#!/usr/bin/env python
# coding: utf-8

# # TEM(.dm3) and SEM(.tif) to .jpg with metadata
# 
# * hyperspy : http://hyperspy.org/hyperspy-doc/current/user_guide/getting_started.html#starting-hyperspy-in-the-notebook-or-terminal
# * scikit-image (>=0.14.2) : https://scikit-image.org/
# * piexif : https://github.com/hMatoba/Piexif
# * Pillow : https://pillow.readthedocs.io/en/stable/
# * matplotlib-scalebar : https://github.com/ppinard/matplotlib-scalebar

# ### 1. Import libararies

# Import libaries
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import skimage
import hyperspy.api as hs
import hyperspy.drawing.image as hsi
import os, copy, sys
from PIL import Image
from PIL.TiffTags import TAGS
import json

# ### 2. Doing chores

# turn off hyperspy warning signs
hs.preferences.GUIs.warn_if_guis_are_missing = False
hs.preferences.save()

# find working directory
pwd = os.getcwd()
print(pwd)

# ### 3. Function : Metadata Extraction
# 
# - input : input file name
# - output : metadata (dictionary type)
def extmeta_dm3(infilename):
  
  im = hs.load(infilename)
  # File name
  filename = im.metadata.General.original_filename

  # Instrument
  microscope = im.original_metadata.ImageList.TagGroup0.ImageTags.Microscope_Info.Microscope
  mode_acq = im.metadata.Acquisition_instrument.TEM.acquisition_mode
  mode_img = im.original_metadata.ImageList.TagGroup0.ImageTags.Microscope_Info.Imaging_Mode
  beam_nrg = im.metadata.Acquisition_instrument.TEM.beam_energy

  # Acquisition
  acq_date = im.original_metadata.ImageList.TagGroup0.ImageTags.DataBar.Acquisition_Date
  acq_time = im.original_metadata.ImageList.TagGroup0.ImageTags.DataBar.Acquisition_Time
  exp_time = im.original_metadata.ImageList.TagGroup0.ImageTags.DataBar.Exposure_Time_s
  intensity_max = im.original_metadata.ImageList.TagGroup0.ImageTags.Acquisition.Frame.Intensity.Range.Maximum_Value_counts
  intensity_min = im.original_metadata.ImageList.TagGroup0.ImageTags.Acquisition.Frame.Intensity.Range.Minimum_Value_counts

  # Image
  mag = im.metadata.Acquisition_instrument.TEM.magnification
  binning = im.original_metadata.ImageList.TagGroup0.ImageTags.Acquisition.Frame.Area.Transform.Transform_List.TagGroup0.Binning
  #intensity_max = im.original_metadata.ImageList.TagGroup0.ImageTags.Acquisition.Frame.Intensity.Range.Mininum_Value

  scale_x = im.original_metadata.ImageList.TagGroup0.ImageData.Calibrations.Dimension.TagGroup0.Scale
  scale_y = im.original_metadata.ImageList.TagGroup0.ImageData.Calibrations.Dimension.TagGroup1.Scale
  scale_unit = im.original_metadata.ImageList.TagGroup0.ImageData.Calibrations.Dimension.TagGroup0.Units
  if scale_unit == '\u00b5m':
    scale_unit = 'um'

  dim_x = im.original_metadata.ImageList.TagGroup0.ImageData.Dimensions.Data0
  dim_y = im.original_metadata.ImageList.TagGroup0.ImageData.Dimensions.Data1

  #------------------------
  print('#----------------------')
  print('Filename= {}'.format(filename))
  print('- Date= {}'.format(acq_date))
  print('- Time= {}\n'.format(acq_time))

  print('Microscope= {}'.format(microscope))
  print('- Acquisition Mode= {}'.format(mode_acq))
  print('- Imaging Mode= {}'.format(mode_img))
  print('- Bean energy= {} kV'.format(beam_nrg))
  print('- Exposure Time= {} s\n'.format(exp_time))
  print('- Max Intensity= {} counts'.format(intensity_max))
  print('- Min Intensity= {} counts'.format(intensity_min))

  print('- Magnification= x{:4d}'.format(int(mag)))
  print('- Binning= {}'.format(binning))
  print('- Scale (x,y)= ({:2.4f}, {:2.4f})'.format(scale_x, scale_y))
  print('- Scale Units= {}'.format(scale_unit))
  print('- Dimension (x,y)= ({:4d}, {:4d})'.format(dim_x, dim_y))

  scale_key = 'scale (({:})/px)'.format(scale_unit)

  imgdata = {
    'Filename': filename,
    'Acq.Date': acq_date,
    'Acq.Time': acq_time,
    'Microscope': microscope,
    'Acq.Mode': mode_acq,
    'Imaging Mode': mode_img,
    'Beam Energy(kV)': beam_nrg,
    'Exposure Time(s)': exp_time,
    'Max Intensity (count)': intensity_max,
    'Min Intensity (count)': intensity_min,
    'Magnification (X)': mag,
    'Binning': binning,
  #  scale_key: (scale_x, scale_y),
    'scale' : (scale_x, scale_y),
    'scale_unit' : scale_unit,
    'dimension (px,px)': (dim_x, dim_y),
    'image size (px,px)': (dim_x, dim_y)    # for dm3 file, no additional area is assumed
  }

  return imgdata


# get metadata from tif file, for the case of many empty items.
def getmeta_tif(meta_dict: dict, cat1: str, cat2: str):
  if meta_dict.get(cat1) != None:
    if meta_dict.get(cat1).get(cat2) != None and meta_dict.get(cat1).get(cat2) != '':
      return meta_dict.get(cat1).get(cat2)
    else:
      return None
  else:
    return None

  
#  convert metadata as float type, if it is not None 
def getmetaf_tif(meta_dict: dict, cat1: str, cat2: str):
  tmpmeta = getmeta_tif(meta_dict, cat1, cat2)
  return np.nan if (tmpmeta == None) else float(tmpmeta) 


# extract metadata from SEM tif file
def extmeta_tif(infilename):
  
  with Image.open(infilename) as img:
    meta = img.tag
    meta_data = meta[34682]
    meta_dim = [meta[256][0], meta[257][0]]

  result = meta_data
  result = meta_data[0].replace('\r', '", ') 
  result = result.replace('\n', ' "')
  result = result.replace('=', '" : "')
  result = result.replace(']", ', '" : {')
  result = result.replace(',  "",  "[', '}, "')
  result = result.replace('[', '"')
  result = result.replace(',  "",  "', '}')

  if result[-4:] == ',  "':
    result = result[:-4] + '}'
  
  result = '{' + result + '}'
  meta_dict = json.loads(result)  
    
  filename = infilename.split('/')[-1]
  
  acq_date = getmeta_tif(meta_dict, 'User', 'Date')
  acq_time = getmeta_tif(meta_dict, 'User', 'Time')
  microscope = getmeta_tif(meta_dict, 'System', 'Type')
  mode_acq = getmeta_tif(meta_dict, 'Detectors', 'Mode')
  mode_img = getmeta_tif(meta_dict, 'Beam', 'ImageMode')
  
  beam_nrg = getmetaf_tif(meta_dict, 'Beam', 'HV') / 1000 
  beam_cur_1 = getmeta_tif(meta_dict, 'Beam', 'BeamCurrent')
  beam_cur_2 = getmeta_tif(meta_dict, 'EBeam', 'BeamCurrent')
  if beam_cur_1 != None:
    beam_cur = float(beam_cur_1) * 1e12
  elif beam_cur_2 != None:
    beam_cur = float(beam_cur_2) * 1e12
  else:
    beam_cur = None
  
  spot_size = getmetaf_tif(meta_dict, 'Beam', 'Spot')
  
  landing_nrg_1 = getmeta_tif(meta_dict, 'CathodeLens', 'LandingEnergy')
  landing_nrg_2 = getmeta_tif(meta_dict, 'EBeamDeceleration', 'LandingEnergy')
  if landing_nrg_1 != None:
    landing_nrg = float(landing_nrg_1) / 1000
  elif landing_nrg_2 != None:
    landing_nrg = float(landing_nrg_2) / 1000
  else:
    landing_nrg = None
  
  dwell_time = getmetaf_tif(meta_dict, 'Scan', 'Dwelltime') * 1e9
  frame_time = getmetaf_tif(meta_dict, 'Scan', 'FrameTime')
  scale_x = getmetaf_tif(meta_dict, 'Scan', 'PixelWidth') * 1e9
  scale_y = getmetaf_tif(meta_dict, 'Scan', 'PixelHeight') * 1e9
  scale_unit = 'nm'
  scale_key = 'scale (nm/px)'
  len_x = getmetaf_tif(meta_dict, 'Scan', 'HorFieldsize') * 1e6
  len_y = getmetaf_tif(meta_dict, 'Scan', 'VerFieldsize') * 1e6
  image_avg = getmetaf_tif(meta_dict, 'Image', 'Average')
  dim_x = int(getmetaf_tif(meta_dict, 'Image', 'ResolutionX'))
  dim_y = int(getmetaf_tif(meta_dict, 'Image', 'ResolutionY'))
  
  stage_x = getmetaf_tif(meta_dict, 'Stage', 'StageX') * 1e3
  stage_y = getmetaf_tif(meta_dict, 'Stage', 'StageY') * 1e3
  stage_z = getmetaf_tif(meta_dict, 'Stage', 'StageZ') * 1e3
  stage_r = getmetaf_tif(meta_dict, 'Stage', 'StageR')
  stage_ta = getmetaf_tif(meta_dict, 'Stage', 'StageT')
  stage_tb = getmetaf_tif(meta_dict, 'Stage', 'StageTb')
  
  stage_tilt = getmetaf_tif(meta_dict, 'Stage', 'SpecTilt')
  work_dist = getmetaf_tif(meta_dict, 'Stage', 'WorkingDistance') * 1e3
  
  img_dim = meta_dim
  
  imgdata = {
    'Filename': filename,
    'Acq.Date': acq_date,
    'Acq.Time': acq_time,
    'Microscope': microscope,
    'Acq.Mode': mode_acq,
    'Imaging Mode': mode_img,
    'Beam Energy (kV)': beam_nrg,
    'Beam Current (pA)' : beam_cur,
    'Landing Energy (kV)' : landing_nrg,
    'Spot Size (nm)' : spot_size,
    'Dwell time (ns)':dwell_time,   
    'Frame Time (s)': frame_time,
    'Image Average': image_avg,
    'Stage X (mm)': stage_x,
    'Stage Y (mm)': stage_y,
    'Stage Z (mm)': stage_z,
    'Stage Rotation (deg)': stage_r,
    'Stage Tilt-alpha (deg)': stage_ta,
    'Stage Tilt-beta (deg)': stage_tb,
    'Stage Tilt (deg)': stage_tilt,
    'Working Distance (mm)': work_dist,
    'scale' : (scale_x, scale_y),
    'scale_unit' : scale_unit,
    'dimension (um,um)': (len_x, len_y),
    'dimension (px,px)': (dim_x, dim_y),
    'image size (px,px)': (meta_dim[0], meta_dim[1])
  }

  return imgdata


# extract metadata from .dm3 or .tif file
def extmeta(infilename):
  
  if infilename[-3:] == 'dm3': 
    return extmeta_dm3(infilename)
  
  elif infilename[-3:] == 'tif' or infilename[-4:] == 'tiff':
    return extmeta_tif(infilename)


# ### 4. Function : Image Processing 
# 
# * Here, simple Auto-Contrast Adjustment
from skimage.io import imsave, imshow, imread
from skimage import exposure
from matplotlib_scalebar.scalebar import ScaleBar
from matplotlib_scalebar.scalebar import SI_LENGTH_RECIPROCAL
from copy import deepcopy

# define scale bar color: black or white
def sb_color(img):
  imga = np.array(img)
  
  bl = imga.shape
  bl_row = int(bl[0] * 0.9)
  bl_col = int(bl[1] * 0.1)
  
  bl_box = imga[bl_row:, :bl_col]
  bl_box_mean = bl_box.mean()
  
  if bl_box_mean < 128:
    return 'w'
  else:
    return 'k'
  
  
# add scale on image
def addscale(img, imgdata, outfile, scale_value='auto'):    # Add Scalebar on TEM  Image
  
  # extract scale bar and scale unit
  scale_x = imgdata['scale'][0]
  scale_y = imgdata['scale'][1]
  scale_ratio = scale_y/scale_x
  scale_unit = imgdata['scale_unit']
  dimension = imgdata['dimension (px,px)']

  # image prepration for new image  
  imga = np.array(img)
  color = sb_color(imga)    # color of scale bar
  dpi = 1000

  fig = plt.figure(figsize=(dimension[0]/dpi, dimension[1]/dpi), frameon=False)
  ax = fig.add_axes([0, 0, 1, 1])
  ax.axis('off')
  location = 'lower left'
  frameon = False
  
  # find optimum scale bar value
  scvs = np.array([1, 2, 5, 10, 20, 50, 100, 200, 500])    # scale bar candidates
  scvs_px = scvs / imgdata['scale'][0] 
  rel_len = imgdata['image size (px,px)'][1] *0.2     # scale bar should close to 20% of image width
  scale_value = scvs[np.argmin(abs(scvs_px - rel_len))]
  print('scale_value= {}'.format(scale_value))

  if scale_unit[0] == '1':    # reciporcal space, such as 1/nm
    scalebar = ScaleBar(scale_x, scale_unit, SI_LENGTH_RECIPROCAL, 
                        location=location, 
                        frameon=frameon,
                        color=color,
                        fixed_value=scale_value
                       )
  else:        # real space
    scalebar = ScaleBar(scale_x, scale_unit,
                        location=location,
                        frameon=frameon,
                        color=color,
                        fixed_value=scale_value
                       )

  plt.imshow(imga)
  plt.gca().add_artist(scalebar)
  plt.savefig(outfile, dpi=dpi)
  
  return outfile
  

# Image Processing and Add Scalebar
def imgproc(infilename, imgdata):    

  outdir = pwd + '/output.dir/' + infilename.split('/')[-2]
  outfile = pwd + '/output.dir/' + infilename.split('/')[0] + '/' + imgdata['Filename'][:-4] + '.jpg'
  outfile_sb = pwd + '/output.dir/' + infilename.split('/')[0] + '/' + imgdata['Filename'][:-4] + '_sb.jpg'
    
  # load image as numpy 2D array
  if infilename[-3:] == 'dm3':
    im = hs.load(infilename)
    img = im.data
  
  elif infilename[-4:] == 'tiff' or infilename[-3:] == 'tif':
    img = imread(infilename)   
    
    if isinstance(img[0][0], list):   # for the case of RGB image,
      img = img[:, :, 0]                     # pick only R channel
    
  # if additional area is added on image, crop that out
  slice_flag= 0
  if (infilename[-4:] == 'tiff' or infilename[-3:] == 'tif') and (imgdata['image size (px,px)'] != imgdata['dimension (px,px)']):
    slice_flag = 1
    img_main = img[: imgdata['dimension (px,px)'][1], : imgdata['dimension (px,px)'][0]]
    img_sub = img[imgdata['dimension (px,px)'][1] : ,  : imgdata['dimension (px,px)'][0]]
    img = copy.deepcopy(img_main)
  
  # Auto contrast
  v_min, v_max = np.percentile(img, (0.2, 99.8))
  img = exposure.rescale_intensity(img, in_range=(v_min, v_max), out_range=(0, 255)).astype(np.uint8)
  if slice_flag == 1:
    img_sub = exposure.rescale_intensity(img_sub, out_range=(0, 255)).astype(np.uint8)
  
  # if splitted, restore
  if slice_flag == 1:
    img_sb = np.vstack((img, img_sub))
  else:
    img_sb = copy.deepcopy(img)

  if not os.path.exists(outdir):
    os.mkdir(outdir)  
    
  print('# Outfile = {}'.format(outfile))
  
  imsave(outfile, img)
  imsave(outfile_sb, img_sb)
  
  if slice_flag != 1:
      outfile_sb = addscale(img, imgdata, outfile_sb, scale_value='auto')

  return outfile, outfile_sb


# ### 5. Function : Add Metadata and Export Image
# 
# * Edit metadata on .jpg file
from PIL import Image
import json
import piexif
import piexif.helper

def addmeta(infilename, imgdata):
  if infilename != None:
    # Load image to edit
    imPIL = Image.open(infilename)

    # For unknown reason, this line prevents strange image shift
    imPIL.save(infilename)    
    imgdump = json.dumps(imgdata)
    user_comment = piexif.helper.UserComment.dump(imgdump)

    # extract Exif data from image
    exif_dict = piexif.load(infilename)
    exif_dict["Exif"][piexif.ExifIFD.UserComment] = user_comment
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, infilename)
    #print(exif_bytes)

    imPIL.save(infilename, exif=exif_bytes)
    plt.imshow(np.asarray(imPIL));
    plt.close()


# ### 7. Run on all .dm3 and .tif files
# 
# load .dm3 image
"""
# directories containing dm3 and tif files
dirs = [file for file in os.listdir(pwd) ]
imgdir = []

for dirname in dirs:
  if '.' not in dirname:
    imgdir.append(dirname)

for d in imgdir:
  # dm3 and tif files
  print('### directory= {}'.format(d))
  files = [file for file in os.listdir(d) ]
  imgfiles = [file for file in files if (file.endswith('.dm3') or file.endswith('.tiff') or file.endswith('tif'))]
  
  for f in imgfiles:
    print('### file= {}'.format(f))
    
    # Main part
    infilename = os.path.join(d,f)    # 1. define file name with directory
    imgdata = extmeta(infilename)    # 2. extract meta data
    outfilename, outfilename_sb = imgproc(infilename, imgdata)    # 3. Image Processing (Auto Contrast, add Scale bar)
    addmeta(outfilename, imgdata)    # 4-1. Add meta data on image only
    addmeta(outfilename_sb, imgdata)    # 4-2. Add meta data on image with scale bar
"""

# ### 8. Run with arguments
if __name__ == "__main__":
    infilename = sys.argv[1]    # 1. define file name with directory
    imgdata = extmeta(infilename)    # 2. extract meta data
    outfilename, outfilename_sb = imgproc(infilename, imgdata)    # 3. Image Processing (Auto Contrast, add Scale bar)
    addmeta(outfilename, imgdata)    # 4-1. Add meta data on image only
    addmeta(outfilename_sb, imgdata)    # 4-2. Add meta data on image with scale bar
