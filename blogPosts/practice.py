#from .static.blogPosts.json import page_section_info
import json 

# mainPageInfo_object = json.loads(page_section_info)
# print (type(mainPageInfo_object))

json_data = open('static/blogPosts/json/page_section_info.json')
data1 = json.load(json_data)
#data1['id']

