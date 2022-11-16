#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 16:50:53 2022

@author: justinkaufman
"""

import numpy as np
import os 
import pydicom as dicom
import matplotlib.pyplot as plt
from fpdf import FPDF
import subprocess
from PIL import Image
import nibabel as nib
import io

from matplotlib.backends.backend_pdf import PdfPages


# =============================================================================
# directory='/Users/justinkaufman/radiology_research/iMRI_Pig_Data/2021_11_17/1117/390'
# 
# 
# 
# # =============================================================================
# # images=[]
# # 
# # for filename in os.listdir(directory):
# #     if filename.endswith('.dcm'):
# #         ds = dicom.dcmread(os.path.join(directory, filename))
# #         image=ds.pixel_array.astype(float)
# #         scaled_image = (np.maximum(image, 0) / image.max()) * 255.0
# #         scaled_image = np.uint8(scaled_image)
# #         final_image = Image.fromarray(scaled_image)
# #         #final_image.show()
# #         images.append(final_image)
# #         #pdf.image(final_image)
# #         
# # 
# # images[0].save(r'/Users/justinkaufman/Desktop/my_images.pdf', save_all=True, append_images=images[1:])
# # 
# # 
# # path='/Users/justinkaufman/Desktop/my_images.pdf'
# # 
# # 
# # subprocess.Popen([path],shell=True)
# # 
# # =============================================================================
# #pdf.image(temp)
#         
# 
# #pdf.output("images.pdf", "F")
# 
# 
# 
# def images_to_pdf(directory):
#     images=[]
# 
#     for filename in sorted(os.listdir(directory)):
#         if filename.endswith('.dcm'):
#             ds = dicom.dcmread(os.path.join(directory, filename))
#             image=ds.pixel_array.astype(float)
#             scaled_image = (np.maximum(image, 0) / image.max()) * 255.0
#             scaled_image = np.uint8(scaled_image)
#             final_image = Image.fromarray(scaled_image)
#             images.append(final_image)
#             
# 
#     images[0].save(r'/Users/justinkaufman/Desktop/my_images.pdf', save_all=True, append_images=images[1:])
# 
# 
# 
# 
# 
# images=[]
# 
# 
# for filename in sorted(os.listdir(directory), reverse=True):
#     if filename.endswith('.dcm'):
#         ds = dicom.dcmread(os.path.join(directory, filename))
#         image=ds.pixel_array.astype(float)
#         scaled_image = (np.maximum(image, 0) / image.max()) * 255.0
#         scaled_image = np.uint8(scaled_image)
#         final_image = Image.fromarray(scaled_image)
#         images.append(final_image)
#         
# 
# images[0].save(r'/Users/justinkaufman/Desktop/my_images.pdf', save_all=True, append_images=images[1:])
# 
# 
# 
# 
# 
# ni_images=[]
# 
# for filename in sorted(os.listdir(directory)):
#     if filename.endswith('.nii'):
#         ni = nib.load(os.path.join(directory, filename)).get_fdata()
#         #print(ni.shape) # 3rd dim is how many slices
#         ni=ni.astype(float)
#         for i in range(ni.shape[2]):
#             scaled_image = (np.maximum(ni[:,:,0+i], 0) / ni[:,:,0+i].max()) * 255.0
#             scaled_image = np.rot90(np.fliplr(np.uint8(scaled_image)))
#             final_image = Image.fromarray(scaled_image)
#             ni_images.append(final_image)
# # =============================================================================
# #         plt.imshow(final_image,cmap='gray')
# #         plt.show()
# # =============================================================================
#         
# ni_images[0].save(r'/Users/justinkaufman/Desktop/nii_images.pdf', save_all=True, append_images=ni_images[1:])
# 
# 
# both_images=[]
# 
# final_images=[]
# 
# for i in range(len(images)):
#     both_images.append(images[i])
#     both_images.append(ni_images[i])
#     widths, heights = zip(*(i.size for i in both_images))
#     total_width = sum(widths)
#     max_height = max(heights)
# 
#     new_im = Image.new('RGB', (total_width, max_height))
# 
#     x_offset = 0
#     for im in both_images:
#       new_im.paste(im, (x_offset,0))
#       x_offset += im.size[0]
#     
#     final_images.append(new_im)
#     both_images=[]
# 
# 
# final_images[0].save(r'/Users/justinkaufman/Desktop/final_images.pdf', save_all=True, append_images=final_images[1:])
# 
# # =============================================================================
# # def main():
# #     #images_to_pdf(directory)
# # 
# # if __name__ == "__main__":
# #     main()
# # =============================================================================
# 
# 
# 
# =============================================================================






directory='/Users/justinkaufman/radiology_research/iMRI_Pig_Data/2021_11_17/1117/390'


def fig2img(fig):
    """Convert a Matplotlib figure to a PIL Image """
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    img = Image.open(buf)
    return img


def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result

def images_to_pdf(directory):
    images=[]


    for filename in sorted(os.listdir(directory), reverse=True):
        if filename.endswith('.dcm'):
            ds = dicom.dcmread(os.path.join(directory, filename))
            image=ds.pixel_array.astype(float)
            scaled_image = (np.maximum(image, 0) / image.max()) * 255.0
            scaled_image = np.uint8(scaled_image)
            final_image = Image.fromarray(scaled_image)
            images.append(final_image)


    ni_images=[]

    for filename in sorted(os.listdir(directory)):
        if filename.endswith('.nii'):
            ni = nib.load(os.path.join(directory, filename)).get_fdata()
            #print(ni.shape) # 3rd dim is how many slices
            ni=ni.astype(float)
            for i in range(ni.shape[2]):
                scaled_image = (np.maximum(ni[:,:,0+i], 0) / ni[:,:,0+i].max()) * 255.0
                scaled_image = np.rot90(np.fliplr(np.uint8(scaled_image)))
                final_image = Image.fromarray(scaled_image)
                ni_images.append(final_image)


    contoured_images=[]

    for i in range(len(images)):
        ax2 = plt.axes()
        ax2.margins(x=0)
        ax2.margins(y=0)
        ax2.axis('off')
        ax2.imshow(images[i], cmap='gray')
        ax2.contour(ni_images[i], colors='red')
        new_ax=fig2img(ax2.figure)
        contoured_images.append(new_ax)
        

    both_images=[]

    final_images=[]

    for i in range(len(images)):
        both_images.append(add_margin(images[i],60,60,52,60,255))
        both_images.append(contoured_images[i])
        widths, heights = zip(*(i.size for i in both_images))
        total_width = sum(widths)
        max_height = max(heights)

        new_im = Image.new('RGB', (total_width, max_height))

        x_offset = 0
        for im in both_images:
          new_im.paste(im, (x_offset,0))
          x_offset += im.size[0]
        
        final_images.append(new_im)
        both_images=[]


    final_images[0].save(r'/Users/justinkaufman/Desktop/final_images.pdf', save_all=True, append_images=final_images[1:])
 


def main():
    images_to_pdf(directory)

if __name__ == "__main__":
    main()

















