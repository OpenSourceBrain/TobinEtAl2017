from pyneuroml.swc.ExportSWC import convert_to_swc

files = ['../nC_projects_lite/PN1LS_allORNs/generatedNeuroML2/neuron_PN1_LS_sk_419138.cell.nml']

for f in files:
    import os 
    cwd = os.path.dirname(os.path.realpath(__file__))
    convert_to_swc(f, add_comments=True, target_dir=cwd)