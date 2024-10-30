from.utils_default_logo_src import DEFAULT_LOGO_SRC
from.utils_template import template_render_infolder
def compare_report_render(meta_dict,data):A={'title':'Comparison Results','color_test':'1982c4','color_reference':'6a4c93','image':DEFAULT_LOGO_SRC,'report_success_collapse':True};A.update(meta_dict);return template_render_infolder('utils_compare_report.html',{'meta':A,'data':data})