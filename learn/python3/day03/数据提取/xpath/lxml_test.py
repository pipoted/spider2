# encode=utf-8

from lxml import etree

text = """
        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/5296774.html" target="_blank" data-index="0" data-lg-tj-id="8E00" data-lg-tj-no=" 0101
                " data-lg-tj-cid="5296774" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                        <h3 style="max-width: 180px;">Python工程师</h3>
                                    <span class="add">[<em>建国门</em>]</span>
                    </a>
                    <span class="format-time">1天前发布</span>
                            <input type="hidden" class="hr_portrait" value="">
                            <input type="hidden" class="hr_name" value="魏晋">
                            <input type="hidden" class="hr_position" value="">
                            <input type="hidden" class="target_hr" value="3537303">
                            <input type="hidden" class="target_position" value="5296774">
                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0101" data-lg-tj-cid="2768" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>
                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">20k-35k</span>
                        <!--<i></i>-->经验5-10年 / 本科
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/2768.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                    0101
                
                " data-lg-tj-cid="2768" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">易到用车</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    移动互联网,O2O / D轮及以上 / 500-2000人
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/2768.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                    0101
                " data-lg-tj-cid="2768" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/47/3B/CgqKkVeO8sWAS9d9AAAgP9GL_Zc630.png" alt="易到用车" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">
            
                <div class="li_b_l">
                            <span>弹性工作</span>
                            <span>带薪年假</span>
                            <span>五险一金</span>
                            <span>补充医疗</span>
                </div>
            <div class="li_b_r">“年底双薪 弹性上班”</div>
        </div>
"""

# html_element = etree.HTML(text)
# # print(type(html_element))
# print(etree.tostring(html_element, encoding='utf-8').decode())

# html_element = etree.parse('job.txt')
# print(etree.tostring(html_element, encoding='utf-8').decode())

def parse_lagou_file():
    parser = etree.HTMLParser(encoding='utf-8')
    html_element = etree.parse('lagou.html', parser=parser)
    print(etree.tostring(html_element, encoding='utf-8').decode())

parse_lagou_file()

