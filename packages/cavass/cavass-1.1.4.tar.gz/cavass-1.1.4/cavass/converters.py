import os
import shutil
from uuid import uuid4

import numpy as np
from jbag.io import save_nifti, ensure_output_file_dir_existence
from jbag.medical_image_converters import nifti2dicom

from cavass.ops import execute_cmd, get_voxel_spacing, read_cavass_file
from cavass.utils import one_hot


def dicom2cavass(input_dir, output_file, offset_value=0):
    """
    Note that if the output file path is too long, this command may be failed.

    Args:
        input_dir (str or pathlib.Path):
        output_file (str or pathlib.Path):
        offset_value (int, optional, default=0):

    """

    assert os.path.exists(input_dir), f'{input_dir} does not exist!'

    made_output_dir, output_dir = ensure_output_file_dir_existence(output_file)

    try:
        r = execute_cmd(f'from_dicom {input_dir}/* {output_file} +{offset_value}')
    except Exception as e:
        if made_output_dir and os.path.isdir(output_dir):
            shutil.rmtree(output_dir)
        else:
            if os.path.exists(output_dir):
                os.remove(output_file)
        raise e

    return r


def nifti2cavass(input_file, output_file, offset_value=0, dicom_accession_number=1):
    """
    Convert NIfTI image to cavass image.

    Args:
        input_file (str or pathlib.Path):
        output_file (str or pathlib.Path):
        offset_value (int, optional, default=0):
        dicom_accession_number (int, optional, default=1):
    """

    assert os.path.isfile(input_file), f'{input_file} does not exist or is not a file!'

    made_output_dir, output_dir = ensure_output_file_dir_existence(output_file)

    tmp_dicom_dir = os.path.join(output_dir, f'{uuid4()}')
    try:
        r1 = nifti2dicom(input_file, tmp_dicom_dir, dicom_accession_number)
        r2 = dicom2cavass(tmp_dicom_dir, output_file, offset_value)
    except Exception as e:
        if made_output_dir and os.path.isdir(output_dir):
            shutil.rmtree(output_dir)
        if os.path.isdir(tmp_dicom_dir):
            shutil.rmtree(tmp_dicom_dir)
        if os.path.exists(output_file):
            os.remove(output_file)

        raise e
    shutil.rmtree(tmp_dicom_dir)
    return r1, r2


def cavass2nifti(input_file, output_file, orientation='ARI'):
    """
    Convert cavass IM0 and BIM formats to NIfTI.

    Args:
        input_file (str or pathlib.Path):
        output_file (str or pathlib.Path):
        orientation (str, optional, default="ARI"): Image orientation of NIfTI file, `ARI` or 'LPI'

    Returns:

    """

    assert os.path.isfile(input_file), f'{input_file} does not exist or is not a file!'

    spacing = get_voxel_spacing(input_file)
    data = read_cavass_file(input_file)
    save_nifti(output_file, data, spacing, orientation=orientation)


def nifti_label2cavass(input_file, output_file, objects, discard_background=True):
    """
    Convert NIfTI format segmentation file to cavass BIM format file. A NIfTI file in where contains arbitrary categories
    of objects will convert to multiple CAVASS BIM files, which matches to the number of object categories.

    Args:
        input_file (str or pathlib.Path):
        output_file (str): The final saved file for category i in input segmentation will be
        `output_file_prefix_{objects[i]}.BIM`
        objects (sequence or str): Objects is an array or a string with comma splitter of object categories,
        where the index of the category in the array is the number that indicates the category in the segmentation.
        discard_background (bool, optional, default True): If True, the regions with label of 0 in the segmentation
        (typically refer to the background region) will not be saved.

    Returns:

    """
    import nibabel as nib

    assert os.path.isfile(input_file), f'{input_file} does not exist or is not a file!'

    input_data = nib.load(input_file)
    image_data = input_data.get_fdata()

    if isinstance(objects, str):
        objects = objects.split(',')
    one_hot_arr = one_hot(image_data, num_classes=len(objects))

    start = 1 if discard_background else 0
    for i in range(start, one_hot_arr.shape[3]):
        nifti_label_image = nib.Nifti1Image(one_hot_arr[..., i], input_data.affine, input_data.header, dtype=np.uint8)
        tmp_nifti_file = f'{output_file}_{objects[i]}.nii.gz'
        made_output_dir, output_dir = ensure_output_file_dir_existence(tmp_nifti_file)
        try:
            nib.save(nifti_label_image, tmp_nifti_file)
            nifti2cavass(tmp_nifti_file, f'{output_file}_{objects[i]}.BIM')
        except Exception as e:
            if made_output_dir and os.path.isdir(output_dir):
                shutil.rmtree(output_dir)
            if os.path.exists(tmp_nifti_file):
                os.remove(tmp_nifti_file)
            raise e
        os.remove(tmp_nifti_file)
