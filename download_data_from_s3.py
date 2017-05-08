

import os


s3getstr = 's3cmd get s3://hcp-openaccess/HCP_900/100307/%s'


base_dir = '/media/sf_SharedFolder/Data/Banff_BIRS_Workshop_Data/data/hcp_100307'


paths = []




# Anatomy 
paths += [ 'MEG/anatomy/100307.L.inflated.4k_fs_LR.surf.gii',
           'MEG/anatomy/100307.L.midthickness.4k_fs_LR.surf.gii',
           'MEG/anatomy/100307.R.inflated.4k_fs_LR.surf.gii',
           'MEG/anatomy/100307.R.midthickness.4k_fs_LR.surf.gii']

# ICA band-limited power Yeo atlas time series 
paths += ['MEG/Restin/icablpenv/100307_MEG_3-Restin_icablpenv_delta.power.Yeo2011.ptseries.nii',      # ICA band-limited power yeo atlas time series
         'MEG/Restin/icablpenv/100307_MEG_3-Restin_icablpenv_theta.power.Yeo2011.ptseries.nii',
         'MEG/Restin/icablpenv/100307_MEG_3-Restin_icablpenv_alpha.power.Yeo2011.ptseries.nii',
         'MEG/Restin/icablpenv/100307_MEG_3-Restin_icablpenv_betalow.power.Yeo2011.ptseries.nii',
	 'MEG/Restin/icablpenv/100307_MEG_3-Restin_icablpenv_betahigh.power.Yeo2011.ptseries.nii',
         'MEG/Restin/icablpenv/100307_MEG_3-Restin_icablpenv_gammalow.power.Yeo2011.ptseries.nii',
         'MEG/Restin/icablpenv/100307_MEG_3-Restin_icablpenv_gammalow.power.Yeo2011.ptseries.nii',
         'MEG/Restin/icablpenv/100307_MEG_3-Restin_icablpenv_gammahigh.power.Yeo2011.ptseries.nii']

# ICA band-limited power all vertex time series
paths += ['MEG/Restin/icablpenv/100307_MEG_3-Restin_icablpenv_whole.power.dtseries.nii']

# (is this needed?)
paths += ['MEG/Restin/icablpenv/Yeo2011_17Networks.LR.min50sqmm.4k_fs_LR.dlabel.nii']


# ICA band-limited power correlation Yeo atlas parcellated connectomes
paths += ['MEG/Restin/icablpcorr/100307_MEG_Restin_icablpcorr_alpha.blpcorr.Yeo2011.pconn.nii',
          'MEG/Restin/icablpcorr/100307_MEG_Restin_icablpcorr_betahigh.blpcorr.Yeo2011.pconn.nii',
          'MEG/Restin/icablpcorr/100307_MEG_Restin_icablpcorr_betalow.blpcorr.Yeo2011.pconn.nii',
          'MEG/Restin/icablpcorr/100307_MEG_Restin_icablpcorr_delta.blpcorr.Yeo2011.pconn.nii',
          'MEG/Restin/icablpcorr/100307_MEG_Restin_icablpcorr_gammahigh.blpcorr.Yeo2011.pconn.nii',
          'MEG/Restin/icablpcorr/100307_MEG_Restin_icablpcorr_gammalow.blpcorr.Yeo2011.pconn.nii',
          'MEG/Restin/icablpcorr/100307_MEG_Restin_icablpcorr_gammamid.blpcorr.Yeo2011.pconn.nii',
          'MEG/Restin/icablpcorr/100307_MEG_Restin_icablpcorr_theta.blpcorr.Yeo2011.pconn.nii',
          'MEG/Restin/icablpcorr/100307_MEG_Restin_icablpcorr_whole.blpcorr.Yeo2011.pconn.nii']


# ICA band-limited power correlation dense connectomes
paths += ['MEG/Restin/icablpcorr/100307_MEG_Restin_icablpcorr_whole.blpcorr.dconn.nii']


# Imaginary coherence Yeo atlas parcellated connectomes
paths += ['MEG/Restin/icaimagcoh/100307_MEG_3-Restin_icaimagcoh_delta.Yeo2011.pconn.nii',
          'MEG/Restin/icaimagcoh/100307_MEG_3-Restin_icaimagcoh_theta.Yeo2011.pconn.nii',
          'MEG/Restin/icaimagcoh/100307_MEG_3-Restin_icaimagcoh_alpha.Yeo2011.pconn.nii',
          'MEG/Restin/icaimagcoh/100307_MEG_3-Restin_icaimagcoh_betalow.Yeo2011.pconn.nii',
          'MEG/Restin/icaimagcoh/100307_MEG_3-Restin_icaimagcoh_betahigh.Yeo2011.pconn.nii',
          'MEG/Restin/icaimagcoh/100307_MEG_3-Restin_icaimagcoh_gammalow.Yeo2011.pconn.nii',
          'MEG/Restin/icaimagcoh/100307_MEG_3-Restin_icaimagcoh_gammamid.Yeo2011.pconn.nii',
          'MEG/Restin/icaimagcoh/100307_MEG_3-Restin_icaimagcoh_gammhigh.Yeo2011.pconn.nii']



# Resting fMRI surface data
paths += ['MNINonLinear/Results/rfMRI_REST1_LR/rfMRI_REST1_LR_Atlas.dtseries.nii']

# Resting fMRI nifti image
paths += ['MNINonLinear/Results/rfMRI_REST1_LR/rfMRI_REST1_LR_hp2000_clean.nii.gz']

# Resting fMRI gifti files
paths += ['MNINonLinear/Results/rfMRI_REST1_LR/rfMRI_REST1_LR.L.native.func.gii',
          'MNINonLinear/Results/rfMRI_REST1_LR/rfMRI_REST1_LR.R.native.func.gii']

# Resting fMRI nifti T1 (?)
paths += ['MNINonLinear/Results/rfMRI_REST1_LR/rfMRI_REST1_LR.nii.gz']


# Anatony
paths += ['MNINonLinear/T1w_restore.nii.gz',
          'MNINonLinear/T1w_restore_brain.nii.gz', 
          'MNINonLinear/T2w_restore.nii.gz',
          'MNINonLinear/T2w_restore_brain.nii.gz',
          'MNINonLinear/aparc+aseg.nii.gz',
          'MNINonLinear/aparc.a2009s+aseg.nii.gz']


cwd = os.getcwd()

for path_it,path in enumerate(paths): 


  folder,fname = os.path.split(path)

  outdir = '%s/%s' %(base_dir,folder)
  
  if not os.path.isdir(outdir):  os.system('mkdir -p %s' %outdir)

  outfile = '%s/%s' %(outdir,fname)
  
  if not os.path.isfile(outfile):

    os.chdir(outdir)
    
    cmd = s3getstr %path 
     
    print '\ndownloading file %s of %s: %s' %(path_it,len(paths),fname)

    os.system(cmd)



os.chdir(cwd)


