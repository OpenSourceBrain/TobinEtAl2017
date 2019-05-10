from pyneuroml.swc.ExportSWC import convert_to_swc

files = ['../nC_projects_lite/PN1LS_allORNs_Rinput/generatedNeuroML2/neuron_PN1_LS_sk_419138.cell.nml',
         '../nC_projects_lite/PN1LS_allORNs/generatedNeuroML2/neuron_PN1_LS_sk_419138.cell.nml',
         '../nC_projects_lite/PN1RS_allORNs/generatedNeuroML2/neuron_PN1_RS_sk_638603.cell.nml',
         '../nC_projects_lite/PN2LS_allORNs/generatedNeuroML2/neuron_PN2_LS_sk_427345.cell.nml',
         '../nC_projects_lite/PN2RS_allORNs/generatedNeuroML2/neuron_PN2_RS_sk_480245.cell.nml',
         '../nC_projects_lite/PN3LS_allORNs/generatedNeuroML2/neuron_PN3_LS_sk_668267.cell.nml']

for f in files:
    import os 
    cwd = os.path.dirname(os.path.realpath(__file__))
    convert_to_swc(f, add_comments=True, target_dir=cwd)