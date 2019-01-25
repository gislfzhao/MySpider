# -*- coding: utf-8 -*-
import re
from pyquery import PyQuery as pq


EARLY_SECTIONS = ['要闻', '国际', '社会', '财经', '文体']
html = """
<div id="img-content">


                    <h2 class="rich_media_title" id="activity-name">


                        早啊！新闻来了〔2019.01.07〕

                    </h2>
                    <div id="meta_content" class="rich_media_meta_list">

                                        <span class="rich_media_meta rich_media_meta_nickname" id="profileBt">
                      <a href="javascript:void(0);" id="js_name">
                        知行游学荟                      </a>
                      <div id="js_profile_qrcode" class="profile_container" style="display:none;">
                          <div class="profile_inner">
                              <strong class="profile_nickname">知行游学荟</strong>
                              <img class="profile_avatar" id="js_profile_qrcode_img" src="" alt="">

                              <p class="profile_meta">
                              <label class="profile_meta_label">微信号</label>
                              <span class="profile_meta_value">zhixingyouxue</span>
                              </p>

                              <p class="profile_meta">
                              <label class="profile_meta_label">功能介绍</label>
                              <span class="profile_meta_value">读万卷书，行万里路。我们的产品涵盖非遗研学、自然探索、设计思维、口语表达、心理成长、亲子关系拓展等，有周末的单日活动，也有小长假、寒暑假的国内外游学和冬夏令营，同时，面向班集体和企业提供各种课程及亲子活动的定制服务。</span>
                              </p>

                          </div>
                          <span class="profile_arrow_wrp" id="js_profile_arrow_wrp">
                              <i class="profile_arrow arrow_out"></i>
                              <i class="profile_arrow arrow_in"></i>
                          </span>
                      </div>
                    </span>


                        <em id="publish_time" class="rich_media_meta rich_media_meta_text"></em>


                    </div>


                    <div class="rich_media_content " id="js_content">


                        <section data-role="outer" label="Powered by 135editor.com"
                                 style="font-size: 16px;font-family: 微软雅黑;">
                            <section data-role="outer" label="Powered by 135editor.com"><p style="text-align: center;">
                                <img class="" data-s="300,640"
                                     data-src="https://mmbiz.qpic.cn/mmbiz_jpg/oq1PymRl9D7Xiaj2MuYymth7K0yeOnyBcUfkqEKKwp0ibF990Jb4m2FRy54NIurib3zk0XPoNnRRSvPvZNZpew0iag/640?wx_fmt=jpeg"
                                     data-type="jpeg" data-w="900" data-ratio="0.5555555555555556"/></p>
                                <section class=""
                                         style="white-space: normal;max-width: 100%;letter-spacing: 0.544px;color: rgb(62, 62, 62);line-height: 17.0667px;border-width: 0px;border-style: none;border-color: initial;background-color: rgb(255, 255, 255);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                    <section
                                            style="margin-top: 10px;margin-bottom: 10px;max-width: 100%;border-width: 0px;border-style: initial;border-color: initial;text-align: center;box-sizing: border-box !important;overflow-wrap: break-word !important;transform: skew(-20deg);-webkit-transform: skew(-20deg);-moz-transform: skew(-20deg);-o-transform: skew(-20deg);">
                                        <section class=""
                                                 style="max-width: 100%;display: inline-block;color: rgb(255, 255, 238);border-color: rgb(0, 187, 236);background-color: rgb(0, 187, 236);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                            <section
                                                    style="padding-right: 10px;padding-left: 10px;max-width: 100%;display: inline-block;border-color: rgb(0, 187, 236);color: inherit;background-color: rgba(255, 255, 255, 0.7);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                <section class=""
                                                         style="max-width: 100%;display: inline-block;color: inherit;border-color: rgb(0, 187, 236);background-color: rgb(0, 187, 236);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                    <section
                                                            style="padding-right: 10px;padding-left: 10px;max-width: 100%;display: inline-block;border-color: rgb(0, 187, 236);color: inherit;background-color: rgba(255, 255, 255, 0.498);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                        <section class=""
                                                                 style="max-width: 100%;display: inline-block;color: inherit;border-color: rgb(0, 187, 236);background-color: rgb(0, 187, 236);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                            <section
                                                                    style="padding-right: 10px;padding-left: 10px;max-width: 100%;display: inline-block;border-color: rgb(0, 187, 236);color: inherit;background-color: rgba(255, 255, 255, 0.298);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                                <section class=""
                                                                         style="max-width: 100%;display: inline-block;color: inherit;border-color: rgb(0, 187, 236);background-color: rgb(0, 187, 236);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                                    <h4 style="padding: 10px;max-width: 100%;border-color: rgb(0, 187, 236);color: inherit;box-sizing: border-box !important;overflow-wrap: break-word !important;transform: skew(20deg);-webkit-transform: skew(20deg);-moz-transform: skew(20deg);-o-transform: skew(20deg);">
                                                                        要闻<br/></h4></section>
                                                            </section>
                                                        </section>
                                                    </section>
                                                </section>
                                            </section>
                                        </section>
                                        <p style="margin-top: -1.2em;margin-bottom: 20px;max-width: 100%;min-height: 1em;white-space: pre-wrap;border-top: 2px solid rgb(0, 187, 236);color: inherit;box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                            <br/></p></section>
                                </section>
                                <ul class=" list-paddingleft-2" style="">
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        中央军委军事工作会议4日在京召开。习近平出席会议并发表重要讲话强调，在新的起点上做好军事斗争准备工作。<a
                                            href="http://mp.weixin.qq.com/s?__biz=MTI0MDU3NDYwMQ==&amp;mid=2656728926&amp;idx=1&amp;sn=82af6555a0dec389a2feb840262c3bdb&amp;chksm=7a608ab84d1703ae3daf6ab3da04b4ede57d95e739977dff81973847f8d1e65f44719bfd714c&amp;scene=21#wechat_redirect"
                                            target="_blank" data-linktype="2"
                                            style="max-width: 100%;font-size: 14px;text-decoration: underline;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span
                                            style="max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;">&gt;&gt;&gt;详情</span></a>
                                    </p></li>
                                </ul>
                                <p style="margin-bottom: 20px;white-space: normal;">
                                    <iframe class="video_iframe" data-vidtype="1"
                                            data-cover="http%3A%2F%2Fshp.qpic.cn%2Fqqvideo_ori%2F0%2Fn0823t0eiic_496_280%2F0"
                                            allowfullscreen="" frameborder="0" data-ratio="1.3333333333333333"
                                            data-w="360"
                                            data-src="https://v.qq.com/iframe/preview.html?width=500&amp;height=375&amp;auto=0&amp;vid=n0823t0eiic"></iframe>
                                </p>
                                <ul class=" list-paddingleft-2" style="">
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        4日上午，习近平签署中央军委2019年1号命令，向全军发布开训动员令。
                                        <a href="http://mp.weixin.qq.com/s?__biz=MTI0MDU3NDYwMQ==&amp;mid=2656728835&amp;idx=1&amp;sn=05aae168f3564d22a77c1e3ca93359d9&amp;chksm=7a608ae54d1703f3ee2c6cd2ae9d93451c51bc59fcd0bca44dbd83d66a1ee7889ccad728f975&amp;scene=21#wechat_redirect"
                                            target="_blank" data-linktype="2"
                                            style="max-width: 100%;font-size: 14px;text-decoration: underline;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span
                                            style="max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;">&gt;&gt;&gt;详情</span></a>
                                    </p></li>
                                </ul>
                                <p style="margin-bottom: 20px;white-space: normal;text-align: center;"><img class=""
                                                                                                            data-copyright="0"
                                                                                                            data-s="300,640"
                                                                                                            data-src="https://mmbiz.qpic.cn/mmbiz_jpg/oq1PymRl9D7Xiaj2MuYymth7K0yeOnyBcgNa63nOYosdMqPueVyegd7KPChbaQWKNqNQjPu8lH7aC73dbOmCqdA/640?wx_fmt=jpeg"
                                                                                                            data-type="jpeg"
                                                                                                            data-w="1080"
                                                                                                            data-ratio="0.6129629629629629"/>
                                </p>
                                <ul class=" list-paddingleft-2" style="">
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        4日，李克强到中国银行、工商银行、建设银行考察，并在银保监会主持召开座谈会。他强调，要加大宏观政策逆周期调节力度，进一步采取减税降费措施，运用好全面降准、定向降准工具，支持民营企业和小微企业融资。</p>
                                    </li>
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        美国国务院日前发布一份关于中国的旅行警告，外交部发言人陆慷4日回应：美方发布的旅行提示经不起推敲。<a
                                            href="http://mp.weixin.qq.com/s?__biz=MTI0MDU3NDYwMQ==&amp;mid=2656728895&amp;idx=1&amp;sn=73a61798855a21eb6c26d2959043bc8f&amp;chksm=7a608ad94d1703cf9781ccc692e65761da41c5c553bdf0754fafc131776f54eaa2b9a9a1afd2&amp;scene=21#wechat_redirect"
                                            target="_blank" data-linktype="2"
                                            style="max-width: 100%;font-size: 14px;text-decoration: underline;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span
                                            style="max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;">&gt;&gt;&gt;详情</span></a>
                                    </p></li>
                                </ul>
                                <p style="margin-bottom: 20px;white-space: normal;line-height: 1.5em;"><img class=""
                                                                                                            data-backh="310"
                                                                                                            data-backw="500"
                                                                                                            data-before-oversubscription-url="https://mmbiz.qpic.cn/mmbiz_jpg/oq1PymRl9D7Xiaj2MuYymth7K0yeOnyBc5IBU5mME6Czj1ICxmhiaBVnwcfPO8QTrSfe5mzfniaaorvACM6BgFUkg/640?wx_fmt=jpeg"
                                                                                                            data-copyright="0"
                                                                                                            data-oversubscription-url="http://mmbiz.qpic.cn/mmbiz_jpg/oq1PymRl9D7Xiaj2MuYymth7K0yeOnyBcfYXe1G5zjZGow9DFoAkvNrrEibPgfXiaApfzYrqv4YoJpps4g19pdFGQ/0?wx_fmt=jpeg"
                                                                                                            data-s="300,640"
                                                                                                            data-src="https://mmbiz.qpic.cn/mmbiz_jpg/oq1PymRl9D7Xiaj2MuYymth7K0yeOnyBcfYXe1G5zjZGow9DFoAkvNrrEibPgfXiaApfzYrqv4YoJpps4g19pdFGQ/640?wx_fmt=jpeg"
                                                                                                            data-type="jpeg"
                                                                                                            data-w="1000"
                                                                                                            style="text-align: center;font-family: -apple-system-font, BlinkMacSystemFont, Arial, sans-serif;width: 100%;"
                                                                                                            data-ratio="0.62"/>
                                </p>
                                <ul class=" list-paddingleft-2" style="">
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        国家航天局消息，嫦娥四号在月背的科学探测工作已陆续展开。“玉兔二号”巡视器择机进入“午休”模式，预计于1月10日唤醒。期间，着陆器将继续正常工作。<a
                                            href="http://mp.weixin.qq.com/s?__biz=MTI0MDU3NDYwMQ==&amp;mid=2656728976&amp;idx=1&amp;sn=0027ade29ac79f86d6b526232aaa0069&amp;chksm=7a608a764d1703607395a83af9015cd67533ba7a614e9a4e25a81258d6d574b312760e1b39ce&amp;scene=21#wechat_redirect"
                                            target="_blank" data-linktype="2"
                                            style="max-width: 100%;font-size: 14px;text-decoration: underline;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span
                                            style="max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;">&gt;&gt;&gt;详情</span></a>
                                    </p></li>
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        据商务部网站4日消息，中美双方将于1月7日至8日举行经贸问题副部级磋商。<a
                                            href="http://mp.weixin.qq.com/s?__biz=MTI0MDU3NDYwMQ==&amp;mid=2656728803&amp;idx=1&amp;sn=dea0d5c4bc2b2fd647b45c7613736119&amp;chksm=7a608b054d17021366e1849898190c12b7ab3b7c22733b099e0574e41dfbe676a12d9f9e042d&amp;scene=21#wechat_redirect"
                                            target="_blank" data-linktype="2"
                                            style="max-width: 100%;font-size: 14px;text-decoration: underline;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span
                                            style="max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;">&gt;&gt;&gt;详情</span></a>
                                    </p></li>
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        5日，全国铁路实施新的列车运行图，近日多条新开通的铁路新线将融入全国高铁网。从5日起，旅客可以通过互联网购买腊月二十九的火车票，车站窗口、代售点推迟两天发售。</p>
                                    </li>
                                </ul>
                                <section class=""
                                         style="white-space: normal;max-width: 100%;letter-spacing: 0.544px;color: rgb(62, 62, 62);line-height: 17.0667px;border-width: 0px;border-style: none;border-color: initial;background-color: rgb(255, 255, 255);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                    <section
                                            style="margin-top: 10px;margin-bottom: 10px;max-width: 100%;border-width: 0px;border-style: initial;border-color: initial;text-align: center;box-sizing: border-box !important;overflow-wrap: break-word !important;transform: skew(-20deg);-webkit-transform: skew(-20deg);-moz-transform: skew(-20deg);-o-transform: skew(-20deg);">
                                        <section class=""
                                                 style="max-width: 100%;display: inline-block;color: rgb(255, 255, 238);border-color: rgb(0, 187, 236);background-color: rgb(0, 187, 236);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                            <section
                                                    style="padding-right: 10px;padding-left: 10px;max-width: 100%;display: inline-block;border-color: rgb(0, 187, 236);color: inherit;background-color: rgba(255, 255, 255, 0.7);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                <section class=""
                                                         style="max-width: 100%;display: inline-block;color: inherit;border-color: rgb(0, 187, 236);background-color: rgb(0, 187, 236);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                    <section
                                                            style="padding-right: 10px;padding-left: 10px;max-width: 100%;display: inline-block;border-color: rgb(0, 187, 236);color: inherit;background-color: rgba(255, 255, 255, 0.498);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                        <section class=""
                                                                 style="max-width: 100%;display: inline-block;color: inherit;border-color: rgb(0, 187, 236);background-color: rgb(0, 187, 236);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                            <section
                                                                    style="padding-right: 10px;padding-left: 10px;max-width: 100%;display: inline-block;border-color: rgb(0, 187, 236);color: inherit;background-color: rgba(255, 255, 255, 0.298);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                                <section class=""
                                                                         style="max-width: 100%;display: inline-block;color: inherit;border-color: rgb(0, 187, 236);background-color: rgb(0, 187, 236);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                                    <h4 style="padding: 10px;max-width: 100%;border-color: rgb(0, 187, 236);color: inherit;box-sizing: border-box !important;overflow-wrap: break-word !important;transform: skew(20deg);-webkit-transform: skew(20deg);-moz-transform: skew(20deg);-o-transform: skew(20deg);">
                                                                        国际</h4></section>
                                                            </section>
                                                        </section>
                                                    </section>
                                                </section>
                                            </section>
                                        </section>
                                        <p style="margin-top: -1.2em;margin-bottom: 20px;max-width: 100%;min-height: 1em;white-space: pre-wrap;border-top: 2px solid rgb(0, 187, 236);color: inherit;box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                            <br/></p></section>
                                </section>
                                <ul class=" list-paddingleft-2" style="">
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        当地时间3日晚，美国众议院投票通过了新的政府预算案，但由于该预算案未包含向美墨边境墙拨款的内容，参院多数党领袖、共和党人麦康奈尔表示参院将不会通过该预算案。</p>
                                    </li>
                                </ul>
                                <p style="white-space: normal;text-align: left;"><img class="" data-copyright="0"
                                                                                      data-s="300,640"
                                                                                      data-src="https://mmbiz.qpic.cn/mmbiz_jpg/oq1PymRl9D7Xiaj2MuYymth7K0yeOnyBcld8J7HqI0s9jxSBcNiciaqd0rgtwzibmgx3keUFztYH4ngF5SiciaTBiapwQ/640?wx_fmt=jpeg"
                                                                                      data-type="jpeg" data-w="1080"
                                                                                      data-ratio="0.6666666666666666"/>
                                </p>
                                <p style="margin-bottom: 20px;white-space: normal;text-align: left;"><span
                                        style="font-size: 14px;color: #888888;">△美墨边境墙/资料图</span></p>
                                <ul class=" list-paddingleft-2" style="">
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        伊朗半官方迈赫尔通讯社4日报道称，伊朗海军副总司令穆加达穆将军当天表示，伊朗海军舰队将于不久后前往大西洋执行任务。</p></li>
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        据俄媒4日报道，巴西总统博尔索纳罗日前在接受采访时表示，他不排除会与美国讨论在巴西建立美国军事基地。</p></li>
                                </ul>
                                <p style="margin-bottom: 20px;white-space: normal;text-align: left;"><img class=""
                                                                                                          data-copyright="0"
                                                                                                          data-s="300,640"
                                                                                                          data-src="https://mmbiz.qpic.cn/mmbiz_jpg/oq1PymRl9D7Xiaj2MuYymth7K0yeOnyBcu4EBNrEEJkbNzsQ8WfuVFicKibmzxPgOMTU1VLtP1Bs5V4DubxQS2ujQ/640?wx_fmt=jpeg"
                                                                                                          data-type="jpeg"
                                                                                                          data-w="1080"
                                                                                                          data-ratio="0.6666666666666666"/><span
                                        style="font-size: 14px;color: #888888;">△博尔索纳罗/资料图</span></p>
                                <ul class=" list-paddingleft-2" style="">
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        菲律宾官方3日消息，近日连续强降雨引发的各类灾害在菲律宾已造成122人遇难，另有28人失踪。</p></li>
                                </ul>
                                <p style="white-space: normal;text-align: center;"><img class="" data-copyright="0"
                                                                                        data-s="300,640"
                                                                                        data-src="https://mmbiz.qpic.cn/mmbiz_jpg/oq1PymRl9D7Xiaj2MuYymth7K0yeOnyBcUz2tPJaRQkY5P0SCxQttKhXcH9kp0WYNONjibVmmGg9Zp5BOtXlScjQ/640?wx_fmt=jpeg"
                                                                                        data-type="jpeg" data-w="1080"
                                                                                        data-ratio="0.5611111111111111"/>
                                </p>
                                <p style="margin-bottom: 20px;white-space: normal;line-height: 1.5em;"><span
                                        style="font-size: 14px;color: #888888;">△2018年12月29日凌晨，台风“乌斯曼”在菲东三描省登陆，由于其移动缓慢且携带大量、持续降雨，导致菲律宾中部和北部多地发生泥石流。</span><br/>
                                </p>
                                <ul class=" list-paddingleft-2" style="">
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;"><span
                                            style="font-family: -apple-system-font, BlinkMacSystemFont, Arial, sans-serif;">日本首相安倍晋三4日下午举行新年记者会，宣布将在4月1日的内阁会议上决定新天皇的新年号。</span>
                                    </p></li>
                                </ul>
                                <p style="margin-bottom: 20px;white-space: normal;text-align: left;"><img class=""
                                                                                                          data-copyright="0"
                                                                                                          data-s="300,640"
                                                                                                          data-src="https://mmbiz.qpic.cn/mmbiz_jpg/oq1PymRl9D7Xiaj2MuYymth7K0yeOnyBcs4lUSxSs3IkhApeg944CJB6rYjkuCJ1iaLLy7SVCzjvibmKwbFhhicCBA/640?wx_fmt=jpeg"
                                                                                                          data-type="jpeg"
                                                                                                          data-w="1080"
                                                                                                          data-ratio="0.775"/><span
                                        style="font-size: 14px;color: #888888;">△安倍晋三/资料图</span></p>
                                <ul class=" list-paddingleft-2" style="">
                                    <li><p style="margin-bottom: 20px;">
                                        当地时间3日，俄罗斯救援人员结束了对车里雅宾斯克州居民楼坍塌现场的搜救工作，此次因燃气爆炸导致的事故共造成39人遇难，其中包括6名儿童。</p></li>
                                </ul>
                                <p style="text-align: center;margin-bottom: 20px;"><img class="" data-backh="340"
                                                                                        data-backw="528"
                                                                                        data-before-oversubscription-url="https://mmbiz.qpic.cn/mmbiz_jpg/oq1PymRl9D7Xiaj2MuYymth7K0yeOnyBcicQ5B6zdMJric4BIk9oKvwSYNWtgTfmOSqrNzD5f7LFEm97icPq3bLB1w/0?wx_fmt=jpeg"
                                                                                        data-copyright="0"
                                                                                        data-s="300,640"
                                                                                        data-src="https://mmbiz.qpic.cn/mmbiz_jpg/oq1PymRl9D7Xiaj2MuYymth7K0yeOnyBcicQ5B6zdMJric4BIk9oKvwSYNWtgTfmOSqrNzD5f7LFEm97icPq3bLB1w/640?wx_fmt=jpeg"
                                                                                        data-type="jpeg" data-w="1080"
                                                                                        style="width: 100%;"
                                                                                        data-ratio="0.6425925925925926"/>
                                </p>
                                <ul class=" list-paddingleft-2" style="">
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        据泰国气象厅4日发布的消息，2019年第一号台风“帕布”已降级为热带低气压，不过仍给泰国南部附近海域带来大风大浪，预计泰国南部多地可能遭遇强降雨。</p>
                                    </li>
                                </ul>
                                <p style="white-space: normal;margin-bottom: 20px;"><img class="" data-copyright="0"
                                                                                         data-src="https://mmbiz.qpic.cn/mmbiz_gif/oq1PymRl9D7Xiaj2MuYymth7K0yeOnyBcQXntZn6iaDNibZARg1nxuKYufGwdqNLUqthk0cfniaAcTOic9Pwm4AtoEg/640?wx_fmt=gif"
                                                                                         data-type="gif" data-w="320"
                                                                                         style="text-align: center;font-family: -apple-system-font, BlinkMacSystemFont, Arial, sans-serif;width: 100%;"
                                                                                         data-backw="320"
                                                                                         data-backh="226"
                                                                                         data-before-oversubscription-url="https://mmbiz.qpic.cn/mmbiz_gif/oq1PymRl9D7Xiaj2MuYymth7K0yeOnyBcQXntZn6iaDNibZARg1nxuKYufGwdqNLUqthk0cfniaAcTOic9Pwm4AtoEg/640?wx_fmt=gif"
                                                                                         data-ratio="0.70625"/></p>
                                <ul class=" list-paddingleft-2" style="">
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        据印度媒体3日报道，首都新德里一工厂日前发生了一起爆炸事件，导致工厂部分建筑垮塌，至少7人死亡，另有8人受伤。</p></li>
                                </ul>
                                <p style="margin-bottom: 20px;white-space: normal;text-align: center;"><img class=""
                                                                                                            data-copyright="0"
                                                                                                            data-s="300,640"
                                                                                                            data-src="https://mmbiz.qpic.cn/mmbiz_png/oq1PymRl9D7Xiaj2MuYymth7K0yeOnyBcibYwlrFmxrmqRiarlXzJxtdsvSiapahNqYnKrnicSgk55j6DKiaqQzwEJHg/640?wx_fmt=png"
                                                                                                            data-type="png"
                                                                                                            data-w="1080"
                                                                                                            data-ratio="0.7111111111111111"/>
                                </p>
                                <ul class=" list-paddingleft-2" style="">
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        澳大利亚东海岸伍伦贡市4日上午发生了一起油罐车起火事故，100名消防员花了数小时才将大火扑灭。据悉，事故没有造成人员伤亡，起火原因正在调查中。</p></li>
                                </ul>
                                <p style="margin-bottom: 20px;white-space: normal;line-height: 1.5em;"><img class=""
                                                                                                            data-copyright="0"
                                                                                                            data-src="https://mmbiz.qpic.cn/mmbiz_gif/oq1PymRl9D7Xiaj2MuYymth7K0yeOnyBc90ZEnO11IKHicGtvBicKGUawJZGbBnAqok3CrqBpibhtptAd7FznzzbBg/640?wx_fmt=gif"
                                                                                                            data-type="gif"
                                                                                                            data-w="320"
                                                                                                            style="text-align: center;font-family: -apple-system-font, BlinkMacSystemFont, Arial, sans-serif;width: 100%;"
                                                                                                            data-backw="320"
                                                                                                            data-backh="228"
                                                                                                            data-before-oversubscription-url="https://mmbiz.qpic.cn/mmbiz_gif/oq1PymRl9D7Xiaj2MuYymth7K0yeOnyBc90ZEnO11IKHicGtvBicKGUawJZGbBnAqok3CrqBpibhtptAd7FznzzbBg/640?wx_fmt=gif"
                                                                                                            data-ratio="0.7125"/>
                                </p>
                                <ul class=" list-paddingleft-2" style="">
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        中国驻新加坡大使馆4日发布公告，提醒中国公民注意遵守当地最新禁烟规定。本月起，新加坡市中心乌节路公共场所开始实施禁烟，吸烟者只能在划有黄线的专设区域内吸烟。违者最高罚款1000新加坡元。</p>
                                    </li>
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        第17届亚洲杯将于2019年1月5日在阿联酋阿布扎比开幕。本届亚洲杯由上一届的16支扩军至24支球队参加比赛，中国队与韩国、吉尔吉斯斯坦、菲律宾一道被分在了C组。<br/>
                                    </p></li>
                                </ul>
                                <section class=""
                                         style="white-space: normal;max-width: 100%;letter-spacing: 0.544px;color: rgb(62, 62, 62);line-height: 17.0667px;border-width: 0px;border-style: none;border-color: initial;background-color: rgb(255, 255, 255);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                    <section
                                            style="margin-top: 10px;margin-bottom: 10px;max-width: 100%;border-width: 0px;border-style: initial;border-color: initial;text-align: center;box-sizing: border-box !important;overflow-wrap: break-word !important;transform: skew(-20deg);-webkit-transform: skew(-20deg);-moz-transform: skew(-20deg);-o-transform: skew(-20deg);">
                                        <section class=""
                                                 style="max-width: 100%;display: inline-block;color: rgb(255, 255, 238);border-color: rgb(0, 187, 236);background-color: rgb(0, 187, 236);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                            <section
                                                    style="padding-right: 10px;padding-left: 10px;max-width: 100%;display: inline-block;border-color: rgb(0, 187, 236);color: inherit;background-color: rgba(255, 255, 255, 0.7);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                <section class=""
                                                         style="max-width: 100%;display: inline-block;color: inherit;border-color: rgb(0, 187, 236);background-color: rgb(0, 187, 236);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                    <section
                                                            style="padding-right: 10px;padding-left: 10px;max-width: 100%;display: inline-block;border-color: rgb(0, 187, 236);color: inherit;background-color: rgba(255, 255, 255, 0.498);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                        <section class=""
                                                                 style="max-width: 100%;display: inline-block;color: inherit;border-color: rgb(0, 187, 236);background-color: rgb(0, 187, 236);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                            <section
                                                                    style="padding-right: 10px;padding-left: 10px;max-width: 100%;display: inline-block;border-color: rgb(0, 187, 236);color: inherit;background-color: rgba(255, 255, 255, 0.298);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                                <section class=""
                                                                         style="max-width: 100%;display: inline-block;color: inherit;border-color: rgb(0, 187, 236);background-color: rgb(0, 187, 236);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                                    <h4 style="padding: 10px;max-width: 100%;border-color: rgb(0, 187, 236);color: inherit;box-sizing: border-box !important;overflow-wrap: break-word !important;transform: skew(20deg);-webkit-transform: skew(20deg);-moz-transform: skew(20deg);-o-transform: skew(20deg);">
                                                                        <span style="max-width: 100%;font-family: 宋体;box-sizing: border-box !important;overflow-wrap: break-word !important;">社会</span>
                                                                    </h4></section>
                                                            </section>
                                                        </section>
                                                    </section>
                                                </section>
                                            </section>
                                        </section>
                                        <p style="margin-top: -1.2em;margin-bottom: 20px;max-width: 100%;min-height: 1em;white-space: pre-wrap;border-top: 2px solid rgb(0, 187, 236);color: inherit;box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                            <br/></p></section>
                                </section>
                                <ul class=" list-paddingleft-2" style="">
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        国家税务总局4日发布通知，要求涉税专业服务机构不得借个人所得税改革实施之机乱收费、高收费，不得蒙蔽纳税人或扣缴义务人谋取不当经济利益，损害纳税人或扣缴义务人合法权益。</p>
                                    </li>
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        教育部4日印发通知，从招生政策、招生程序、加强监管等方面提出了规范高校自主招生的“十严格”要求，包括严格执行公开公示、严格新生复查等。</p></li>
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        民政部日前发布通知，明确规定各级民政部门不再受理养老机构设立许可申请。按照《通知》要求，取消养老机构设立许可后，设立民办公益性养老机构，依法向县级以上地方政府民政部门申请社会服务机构登记。<br/>
                                    </p></li>
                                    <li><p style="margin-top: 20px;margin-bottom: 20px;line-height: 1.5em;">
                                        日前，广东省委原常委、统战部原部长曾志权被双开。<a
                                            href="http://mp.weixin.qq.com/s?__biz=MTI0MDU3NDYwMQ==&amp;mid=2656728952&amp;idx=2&amp;sn=f8eb0be8ae736605a5f47c003ef23e5e&amp;chksm=7a608a9e4d17038802e7893d5c5a0390f993e1a08dccd72c9667a55719b898c59b94dad20647&amp;scene=21#wechat_redirect"
                                            target="_blank" data-linktype="2"
                                            style="max-width: 100%;font-size: 14px;text-decoration: underline;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span
                                            style="max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;">&gt;&gt;&gt;详情</span></a>
                                    </p></li>
                                </ul>
                                <p style="margin-bottom: 20px;white-space: normal;text-align: center;"><img class=""
                                                                                                            data-copyright="0"
                                                                                                            data-s="300,640"
                                                                                                            data-src="https://mmbiz.qpic.cn/mmbiz_jpg/oq1PymRl9D7Xiaj2MuYymth7K0yeOnyBcNy6NYQmXCJMicI2ZsOLuvafXiawDcfZ37BzoWNy9EyJLtx3TdpTxZBKA/640?wx_fmt=jpeg"
                                                                                                            data-type="jpeg"
                                                                                                            data-w="680"
                                                                                                            data-ratio="0.5691176470588235"/>
                                </p>
                                <ul class=" list-paddingleft-2" style="">
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        今年9月30日前，北京大兴国际机场将正式投入使用。日前，中国民航局对外公布方案：新机场投运后，初期将仅安排少量航班运行，在2022年北京冬奥会之前完成全部转场工作。</p>
                                    </li>
                                </ul>
                                <p style="white-space: normal;text-align: center;"><img class="" data-copyright="0"
                                                                                        data-s="300,640"
                                                                                        data-src="https://mmbiz.qpic.cn/mmbiz_png/oq1PymRl9D7Xiaj2MuYymth7K0yeOnyBcr1ic5NchVoQCiaFE7ezMScEc9geSibpdW6JGgMsbAH4jPHEo2wgJpiaRMA/640?wx_fmt=png"
                                                                                        data-type="png" data-w="1080"
                                                                                        data-ratio="0.41388888888888886"/>
                                </p>
                                <p style="margin-bottom: 20px;white-space: normal;line-height: 1.5em;"><span
                                        style="font-size: 14px;color: #888888;">△东航、南航以新机场为主基地，国航以首都机场为主基地</span></p>
                                <ul class=" list-paddingleft-2" style="">
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        北京公安部门消息，2018年9月以来，北京公安局环食药旅总队联合多部门在全市范围内深化开展打击欺诈骗取医疗保障基金专项行动，期间打掉涉案团伙10个，刑事拘留103人，涉案金额5000余万元。</p>
                                    </li>
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        北京生态环境局消息，2018年北京市优良天数227天，一级天同比增加6天，重污染日同比减少9天。2018年全年首次无持续3天及以上的重污染过程。</p>
                                    </li>
                                </ul>
                                <p style="margin-bottom: 20px;white-space: normal;text-align: center;"><img class=""
                                                                                                            data-copyright="0"
                                                                                                            data-s="300,640"
                                                                                                            data-src="https://mmbiz.qpic.cn/mmbiz_jpg/oq1PymRl9D7Xiaj2MuYymth7K0yeOnyBceO2BXwhHSJ41iaHWLZtc1dFpJg7SgHkFCfXPjQkWh0ibx6T5HtSHpNoA/640?wx_fmt=jpeg"
                                                                                                            data-type="jpeg"
                                                                                                            data-w="1080"
                                                                                                            data-ratio="0.6990740740740741"/>
                                </p>
                                <ul class=" list-paddingleft-2" style="">
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        按照天津市委、市政府统一部署，天津市市场监管委会同市政法委、市卫健委等10部门从即日起发起为期3个月的打击、清理整顿保健品乱象专项整治行动。<br/></p>
                                    </li>
                                </ul>
                                <p style="margin-bottom: 20px;white-space: normal;text-align: left;"><img class=""
                                                                                                          data-copyright="0"
                                                                                                          data-s="300,640"
                                                                                                          data-src="https://mmbiz.qpic.cn/mmbiz_jpg/oq1PymRl9D7Xiaj2MuYymth7K0yeOnyBcUFquRQBIYMtZUryhiatbVlqcklxqQCeSztVDrRZqh9lOYIicKAiboukJA/640?wx_fmt=jpeg"
                                                                                                          data-type="jpeg"
                                                                                                          data-w="1080"
                                                                                                          data-ratio="0.6675925925925926"/><span
                                        style="font-size: 14px;color: #888888;">△此次专项整治行动通过“88908890”热线电话和官方网站等，及时回应并处理消费者投诉，举报有奖。</span>
                                </p>
                                <ul class=" list-paddingleft-2" style="">
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        4日凌晨，中国香港籍杂货船“银安”轮与福建晋江籍渔船“闽晋渔05568”轮在福建省平潭牛山岛东南约10海里处发生碰撞事故，造成“闽晋渔05568”轮沉没，船上14名船员落水。目前已有6名船员安全获救，其余8人失踪。</p>
                                    </li>
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        4日上午，浙江省温州市中级人民法院依法不公开开庭审理“滴滴顺风车司机杀人”案，首次组成七人合议庭审理。被告人对指控事实供认不讳，对其犯罪行为表示后悔，愿意接受法律制裁。</p>
                                    </li>
                                </ul>
                                <p style="white-space: normal;text-align: center;"><img class="" data-copyright="0"
                                                                                        data-s="300,640"
                                                                                        data-src="https://mmbiz.qpic.cn/mmbiz_jpg/oq1PymRl9D7Xiaj2MuYymth7K0yeOnyBcMLjoUC0Yze9TWnX46mZ52ChtIFE1CEb9frLsvQPJvlMLzltSwt73jQ/640?wx_fmt=jpeg"
                                                                                        data-type="jpeg" data-w="600"
                                                                                        data-ratio="0.6633333333333333"/>
                                </p>
                                <p style="margin-bottom: 20px;white-space: normal;line-height: 1.5em;"><span
                                        style="font-size: 14px;color: #888888;">△2018年8月24日，被告人钟元在从事滴滴顺风车业务时，采取持刀威胁、胶带捆绑的方式，对乘客被害人赵某某实施了抢劫、强奸行为后杀人灭口。</span>
                                </p>
                                <ul class=" list-paddingleft-2" style="">
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;"><span
                                            style="letter-spacing: 0.544px;background-color: #FFFFFF;">中央气象</span>台预计，4日夜间至5日白天，受冷空气影响，华北中南部、黄淮等地霾天气有所减弱，但黄淮西部、江汉等地的部分地区受输送影响，霾天气将会短时加重，汾渭平原等地的霾天气还将持续。
                                    </p></li>
                                </ul>
                                <p style="margin-bottom: 20px;white-space: normal;text-align: center;"><img class=""
                                                                                                            data-copyright="0"
                                                                                                            data-s="300,640"
                                                                                                            data-src="https://mmbiz.qpic.cn/mmbiz_jpg/oq1PymRl9D7Xiaj2MuYymth7K0yeOnyBcibAMibsOTmfjxWpkNBbT1ibXuicQPSkYzEuybonV1Aakheagwq1Mpc0hAQ/640?wx_fmt=jpeg"
                                                                                                            data-type="jpeg"
                                                                                                            data-w="860"
                                                                                                            data-ratio="0.8104651162790698"/>
                                </p>
                                <section class=""
                                         style="white-space: normal;max-width: 100%;letter-spacing: 0.544px;color: rgb(62, 62, 62);line-height: 17.0667px;border-width: 0px;border-style: none;border-color: initial;background-color: rgb(255, 255, 255);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                    <section
                                            style="margin-top: 10px;margin-bottom: 10px;max-width: 100%;border-width: 0px;border-style: initial;border-color: initial;text-align: center;box-sizing: border-box !important;overflow-wrap: break-word !important;transform: skew(-20deg);-webkit-transform: skew(-20deg);-moz-transform: skew(-20deg);-o-transform: skew(-20deg);">
                                        <section class=""
                                                 style="max-width: 100%;display: inline-block;color: rgb(255, 255, 238);border-color: rgb(0, 187, 236);background-color: rgb(0, 187, 236);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                            <section
                                                    style="padding-right: 10px;padding-left: 10px;max-width: 100%;display: inline-block;border-color: rgb(0, 187, 236);color: inherit;background-color: rgba(255, 255, 255, 0.7);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                <section class=""
                                                         style="max-width: 100%;display: inline-block;color: inherit;border-color: rgb(0, 187, 236);background-color: rgb(0, 187, 236);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                    <section
                                                            style="padding-right: 10px;padding-left: 10px;max-width: 100%;display: inline-block;border-color: rgb(0, 187, 236);color: inherit;background-color: rgba(255, 255, 255, 0.498);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                        <section class=""
                                                                 style="max-width: 100%;display: inline-block;color: inherit;border-color: rgb(0, 187, 236);background-color: rgb(0, 187, 236);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                            <section
                                                                    style="padding-right: 10px;padding-left: 10px;max-width: 100%;display: inline-block;border-color: rgb(0, 187, 236);color: inherit;background-color: rgba(255, 255, 255, 0.298);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                                <section class=""
                                                                         style="max-width: 100%;display: inline-block;color: inherit;border-color: rgb(0, 187, 236);background-color: rgb(0, 187, 236);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                                    <h4 style="padding: 10px;max-width: 100%;border-color: rgb(0, 187, 236);color: inherit;box-sizing: border-box !important;overflow-wrap: break-word !important;transform: skew(20deg);-webkit-transform: skew(20deg);-moz-transform: skew(20deg);-o-transform: skew(20deg);">
                                                                        财经</h4></section>
                                                            </section>
                                                        </section>
                                                    </section>
                                                </section>
                                            </section>
                                        </section>
                                        <p style="margin-top: -1.2em;margin-bottom: 20px;max-width: 100%;min-height: 1em;white-space: pre-wrap;border-top: 2px solid rgb(0, 187, 236);color: inherit;box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                            <br/></p></section>
                                </section>
                                <ul class=" list-paddingleft-2" style="">
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        中国人民银行决定下调金融机构存款准备金率1个百分点，其中，2019年1月15日和1月25日分别下调0.5个百分点，净释放约8000亿元长期资金。<span
                                            style="max-width: 100%;font-size: 14px;text-decoration: underline;box-sizing: border-box !important;overflow-wrap: break-word !important;"><a
                                            href="http://mp.weixin.qq.com/s?__biz=MTI0MDU3NDYwMQ==&amp;mid=2656728952&amp;idx=1&amp;sn=ef070f30ea7b2a70ec89f33aaaad55c5&amp;chksm=7a608a9e4d170388f310ee48c42ce428a9b746b2f55081bb96f37bfc3bcb684e4bbdd1c2dc7b&amp;scene=21#wechat_redirect"
                                            target="_blank" data-linktype="2"
                                            style="max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;">&gt;&gt;&gt;详情</a></span>
                                    </p></li>
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        证监会新闻发言人高莉4日表示，证监会于近日批准开展天然橡胶、棉花和玉米期权交易，2019年1月28日正式挂牌交易。</p></li>
                                </ul>
                                <p style="margin-bottom: 20px;white-space: normal;text-align: center;"><img class=""
                                                                                                            data-copyright="0"
                                                                                                            data-s="300,640"
                                                                                                            data-src="https://mmbiz.qpic.cn/mmbiz_jpg/oq1PymRl9D7Xiaj2MuYymth7K0yeOnyBch4q1BSATN22pqOf3a0K1vktFgofb1EOkW8EaxLWrHJLMEBZ7CiccxHQ/640?wx_fmt=jpeg"
                                                                                                            data-type="jpeg"
                                                                                                            data-w="1080"
                                                                                                            data-ratio="0.6675925925925926"/>
                                </p>
                                <ul class=" list-paddingleft-2" style="">
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        近日，海南航空、大新华航空、深圳航空、祥鹏航空、中国联航、山东航空等航空公司相继对外公布，自2019年1月5日(含出票日期)起，暂停收取国内航线旅客运输燃油附加费。<br/>
                                    </p></li>
                                </ul>
                                <p style="margin-bottom: 20px;white-space: normal;text-align: center;"><img class=""
                                                                                                            data-copyright="0"
                                                                                                            data-s="300,640"
                                                                                                            data-src="https://mmbiz.qpic.cn/mmbiz_jpg/oq1PymRl9D7Xiaj2MuYymth7K0yeOnyBccfhyLwFqhWWOQU5nDhE1vX28Ng7ZePsYicZsSnt0cZ5x52VQgz8VSxg/640?wx_fmt=jpeg"
                                                                                                            data-type="jpeg"
                                                                                                            data-w="1080"
                                                                                                            data-ratio="0.6675925925925926"/>
                                </p>
                                <ul class=" list-paddingleft-2" style="">
                                    <li><p style="margin-bottom: 20px;line-height: 1.5em;">
                                        4日是A股开年后迎来的第三个交易日，早盘沪深两市双双低开，沪指直接击穿2449点创逾4年新低，随后以券商股为首的非银金融板块强势上攻，带动沪指成功翻红并收复2500点，三大股指均大涨逾2%。</p>
                                    </li>
                                </ul>
                                <p style="margin-bottom: 20px;white-space: normal;text-align: center;"><img class=""
                                                                                                            data-copyright="0"
                                                                                                            data-s="300,640"
                                                                                                            data-src="https://mmbiz.qpic.cn/mmbiz_jpg/oq1PymRl9D7Xiaj2MuYymth7K0yeOnyBcNAF5oFOyTDI5HKXqBVfFlLVoRk89rzjWBp81mcXHNZ1WpPKOiayI9Vw/640?wx_fmt=jpeg"
                                                                                                            data-type="jpeg"
                                                                                                            data-w="1080"
                                                                                                            data-ratio="0.8083333333333333"/>
                                </p>
                                <section class="" data-source="bj.96weixin.com"
                                         style="font-family: -apple-system-font, BlinkMacSystemFont, Arial, sans-serif;white-space: normal;max-width: 100%;letter-spacing: 0.544px;background-color: rgb(255, 255, 255);color: rgb(62, 62, 62);line-height: 25.6px;box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                    <section class=""
                                             style="max-width: 100%;border-width: 0px;border-style: none;border-color: initial;box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                        <section class=""
                                                 style="padding: 10px 2px;max-width: 100%;border-style: none none none solid;border-color: rgb(30, 178, 225);line-height: 20px;font-family: arial, helvetica, sans-serif;color: rgb(255, 255, 238);border-radius: 4px;box-shadow: rgb(153, 153, 153) 2px 2px 4px;border-left-width: 10px;background-color: rgb(30, 178, 225);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                            <section
                                                    style="margin-left: 5px;max-width: 100%;display: inline-block;vertical-align: top;border-color: rgb(30, 178, 225);color: inherit;box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                <p style="max-width: 100%;min-height: 1em;white-space: pre-wrap;border-color: rgb(30, 178, 225);color: inherit;box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                    <span style="max-width: 100%;color: inherit;box-sizing: border-box !important;overflow-wrap: break-word !important;">今日提示</span>
                                                </p></section>
                                        </section>
                                    </section>
                                </section>
                                <p style="margin-top: 20px;margin-bottom: 20px;font-family: -apple-system-font, BlinkMacSystemFont, Arial, sans-serif;white-space: normal;max-width: 100%;min-height: 1em;letter-spacing: 0.544px;background-color: rgb(255, 255, 255);caret-color: rgb(51, 51, 51);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                    <strong style="max-width: 100%;white-space: pre-wrap;color: rgb(61, 170, 214);font-size: 20px;line-height: 1.5em;font-family: sans-serif;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span
                                            style="max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><strong
                                            style="max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span
                                            style="max-width: 100%;font-family: 微软雅黑;line-height: 25.6px;box-sizing: border-box !important;overflow-wrap: break-word !important;">●小寒来了！注意预防疾病和意外伤害</span></strong></span></strong>
                                </p>
                                <p style="margin-bottom: 15px;white-space: normal;"><span
                                        style="font-family: -apple-system-font, BlinkMacSystemFont, Arial, sans-serif;">根据《中国天文年历》显示，北京时间1月5日23时39分将迎来农历二十四节气之一的“小寒”，这标志我国气候开始进入一年中最寒冷的时段。</span><br/>
                                </p>
                                <blockquote style="white-space: normal;"><p style="margin-bottom: 10px;"><span
                                        style="font-size: 15px;"><span
                                        style="font-family: arial;font-size: 13px;text-align: start;background-color: #FFFFFF;">①</span>1月份，流感将进入高发期，平时要注意室内通风。</span>
                                </p>
                                    <p style="margin-bottom: 10px;"><span style="font-size: 15px;"><span
                                            style="font-family: arial;font-size: 13px;text-align: start;background-color: #FFFFFF;">②</span>周末外出尽量避免去人多拥挤的公共场所，可及时接种流感疫苗。</span>
                                    </p>
                                    <p style="margin-bottom: 10px;"><span style="font-size: 15px;"><span
                                            style="font-family: arial;font-size: 13px;text-align: start;background-color: #FFFFFF;">③</span>室内干燥，可以使用加湿器增加空气湿度，还可以在暖气片旁边放置清水。</span>
                                    </p>
                                    <p style="margin-bottom: 10px;"><span style="font-size: 15px;"><span
                                            style="font-family: arial;font-size: 13px;text-align: start;background-color: #FFFFFF;">④</span>对于幼儿来说，目前迎来冬季手足口病发病的小高峰，家长要注意防范。</span>
                                    </p>
                                    <p style="margin-bottom: 20px;"><span style="font-size: 15px;"><span
                                            style="font-family: arial;font-size: 13px;text-align: start;background-color: #FFFFFF;">⑤</span>寒潮来袭，雨雪冰冻天气增加，请大家增强自我防护意识，预防疾病和意外伤害。</span>
                                    </p></blockquote>
                                <fieldset class=""
                                          style="margin-top: 0.5em;margin-bottom: 0.5em;white-space: normal;max-width: 100%;min-width: 0px;letter-spacing: 0.544px;background-color: rgb(255, 255, 255);border-width: 0px;border-style: initial;border-top-color: rgb(58, 173, 245);border-right-color: initial;border-bottom-color: initial;border-left-color: initial;line-height: 25.6px;box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                    <section class=""
                                             style="margin-left: 9.26562px;max-width: 100%;border-width: 1px;border-style: solid;border-color: rgb(58, 173, 245);border-radius: 0px 5px 5px 0px;text-align: inherit;text-decoration: inherit;box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                        <section class=""
                                                 style="margin-top: 45.7812px;margin-right: 8px;margin-left: -8px;max-width: 100%;color: rgb(255, 255, 255);font-family: inherit;font-size: 0.8em;float: left;font-style: inherit;text-decoration: inherit;border-color: rgb(58, 173, 245);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                            <span class=""
                                                  style="padding: 0.3em 0.5em;max-width: 100%;display: inline-block;border-radius: 0px 0.5em 0.5em 0px;font-family: inherit;background-color: #3AADF5;box-sizing: border-box !important;overflow-wrap: break-word !important;"><section
                                                    class=""
                                                    style="max-width: 100%;border-top-color: rgb(58, 173, 245);box-sizing: border-box !important;overflow-wrap: break-word !important;"><span
                                                    style="max-width: 100%;font-size: 14px;box-sizing: border-box !important;overflow-wrap: break-word !important;"><strong
                                                    style="max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;">那年今日</strong></span></section></span>
                                            <section class=""
                                                     style="max-width: 100%;width: 0px;border-right: 4px solid rgb(58, 173, 245);border-top: 4px solid rgb(58, 173, 245);box-sizing: border-box !important;overflow-wrap: break-word !important;border-left: 4px solid transparent !important;border-bottom: 4px solid transparent !important;"></section>
                                        </section>
                                        <section class=""
                                                 style="margin-top: 45.7812px;padding-right: 8px;padding-left: 8px;max-width: 100%;text-align: inherit;text-decoration: inherit;border-top-color: rgb(58, 173, 245);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                            <p style="margin-top: 10px;margin-bottom: 20px;max-width: 100%;min-height: 1em;white-space: pre-wrap;border-top-color: rgb(58, 173, 245);box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                <strong style="text-align: inherit;text-decoration: inherit;letter-spacing: 0.544px;white-space: normal;max-width: 100%;color: rgb(0, 176, 240);font-family: 黑体;font-size: 20px;box-sizing: border-box !important;overflow-wrap: break-word !important;">他，保护了25万中国人</strong>
                                            </p>
                                            <p style="margin-bottom: 15px;text-align: center;"><img class=""
                                                                                                    data-copyright="0"
                                                                                                    data-s="300,640"
                                                                                                    data-src="https://mmbiz.qpic.cn/mmbiz_jpg/oq1PymRl9D7Xiaj2MuYymth7K0yeOnyBcibHKgJpthkRCDfdkjUsSa7ahrw4WBUENic0Jw5lV4neSjv3bmg66IDnQ/640?wx_fmt=jpeg"
                                                                                                    data-type="jpeg"
                                                                                                    data-w="350"
                                                                                                    style="height: 365px;width: 253px;"
                                                                                                    data-ratio="1.44"/>
                                            </p>
                                            <p style="margin-bottom: 20px;max-width: 100%;min-height: 1em;box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                                <span style="font-size: 15px;text-align: inherit;text-decoration: inherit;letter-spacing: 0.544px;font-family: -apple-system-font, BlinkMacSystemFont, Arial, sans-serif;">南京大屠杀期间，他奋不顾身阻止暴行，帮助保护25万中国人免遭屠戮；回国后，他因揭露日军罪恶受到纳粹迫害，战后又因曾是纳粹党员入狱。1950年的今天，德国人约翰•拉贝在凄凉孤独中病故。2017年，拉贝的后代将《拉贝日记》原件捐赠给中国。缅怀，铭记！</span><br/>
                                            </p></section>
                                    </section>
                                </fieldset>
                                <section class=""
                                         style="white-space: normal;max-width: 100%;letter-spacing: 0.544px;background-color: rgb(255, 255, 255);line-height: 25.6px;box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                    <p style="margin-top: 20px;margin-bottom: 20px;padding-right: 10px;padding-left: 10px;max-width: 100%;min-height: 1em;color: rgb(40, 170, 240);white-space: pre-wrap;line-height: 25px;border-width: 0px 0px 0px 5px;border-left-color: rgb(40, 170, 240);border-left-style: solid;-webkit-font-smoothing: antialiased;box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                        <strong style="max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;">今日话题</strong>
                                    </p></section>
                                <section class=""
                                         style="white-space: normal;max-width: 100%;letter-spacing: 0.544px;background-color: rgb(255, 255, 255);line-height: 25.6px;box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                    <p style="margin-bottom: 20px;"><span
                                            style="max-width: 100%;font-size: 14px;letter-spacing: 0.544px;white-space: pre-wrap;color: #7F7F7F;line-height: 24px;box-sizing: border-box !important;overflow-wrap: break-word !important;">英国一项针对青少年的最新调查显示，频繁使用社交媒体的少女出现焦虑症状的比例是男孩的两倍，主要原因是女孩更容易受到网络骚扰和睡眠不规律的影响。此外，研究者还发现，女孩在使用社交媒体的过程中更容易受到有关身材、外貌和自尊等方面的影响。为此，有学者呼吁社会及家庭对青少年使用社交媒体的时间进行更严格的控制。对此，你怎么看？</span>
                                    </p>
                                    <p style="margin-bottom: 20px;max-width: 100%;min-height: 1em;text-align: left;line-height: 1.5em;box-sizing: border-box !important;overflow-wrap: break-word !important;">
                                        <br/></p></section>
                            </section>
                        </section>
                    </div>
                    <script nonce="2123278407" type="text/javascript">
                    var first_sceen__time = (+new Date());

                    if ("" == 1 && document.getElementById('js_content')) {
                        document.getElementById('js_content').addEventListener("selectstart",function(e){ e.preventDefault(); });
                    }


                    (function(){
                        if (navigator.userAgent.indexOf("WindowsWechat") != -1){
                            var link = document.createElement('link');
                            var head = document.getElementsByTagName('head')[0];
                            link.rel = 'stylesheet';
                            link.type = 'text/css';
                            link.href = "//res.wx.qq.com/mmbizwap/zh_CN/htmledition/style/page/appmsg_new/winwx42f400.css";
                            head.appendChild(link);
                        }
                    })();

                    </script>


                    <div class="ct_mpda_wrp" id="js_sponsor_ad_area" style="display:none;"></div>


                    <div class="read-more__area" id="js_more_read_area" style="display:none;">

                    </div>


                    <div class="reward_area tc reward_area_primary" id="js_preview_reward_author" style="display:none;">
                        <div class="reward-avatar" style="display: none;" id="js_preview_reward_author_avatar">
                            <img src="" alt="" id="js_preview_reward_author_head">
                        </div>

                        <div class="reward-author" id="js_preview_reward_author_name"></div>
                        <p class="reward_tips" id="js_preview_reward_author_wording" style="display:none;"></p>
                        <p>
                            <a class="reward_button" id='js_preview_reward_author_link' href="##"><span
                                    id="js_preview_reward_link_text">赞赏</span></a>
                        </p>
                    </div>

                    <div class="reward_qrcode_area reward_area tc" id="js_preview_reward_qrcode" style="display:none;">
                        <p class="tips_global">长按二维码向我转账</p>
                        <p id="js_preview_reward_ios_wording" class="reward_tips" style="display:none;"></p>
                        <span class="reward_qrcode_img_wrp"><img class="reward_qrcode_img"
                                                                 src="//res.wx.qq.com/mmbizwap/zh_CN/htmledition/images/pic/appmsg/pic_reward_qrcode.2x42f400.png"></span>
                        <p class="tips_global">受苹果公司新规定影响，微信 iOS 版的赞赏功能被关闭，可通过二维码转账支持公众号。</p>
                    </div>


                </div>
"""

doc = pq(html)
article = doc('#js_content section section')
child = article.children()[0]
article_list = list()
process_result = {
        'section': '',
        'content': '',
        'url': '',
        'image': '',
        'video': '',
        'time': re.search('〔(.*?)〕', doc('#activity-name').text().strip(), re.S).group(1)
    }
while child is not None:
    if child.tag == 'section':
        text = child.text_content().strip()
        if text == '今日提示':
            break
        elif text in EARLY_SECTIONS:
            process_result['section'] = text
    elif child.tag == 'ul':
        lis = child.findall('li')
        if len(lis) > 1:
            for i in range(len(lis) - 1):
                if lis[i].text_content().strip() != '':
                    if lis[i].find('.//a') is not None:
                        process_result['url'] = child.find('.//a').get('href')

                    process_result['content'] = ''.join(lis[i].xpath('./p/text()')).strip()
                    print(process_result)
                    article_list.append(process_result.copy())
                    process_result['url'] = ''
                    process_result['image'] = ''
                    process_result['content'] = ''
                    process_result['video'] = ''

        if lis[len(lis) - 1].find('.//a') is not None:
            process_result['url'] = lis[len(lis) - 1].find('.//a').get('href')
        process_result['content'] = ''.join(lis[len(lis) - 1].xpath('./p/text()')).strip()
        while child.getnext().tag != 'ul' and child.getnext().tag != 'section' and \
                child.getnext().text_content().strip() != '今日提示' \
                and child.getnext().text_content().strip() not in EARLY_SECTIONS:
            child = child.getnext()
            if child.find('iframe') is None:
                if child.find('img') is not None:
                    process_result['image'] = child.find('img').get('data-src')
                else:
                    process_result['content'] += process_result.get('content') + child.text_content().strip()
            else:
                process_result['video'] = child.find('iframe').get('data-src')
        print(process_result)
        article_list.append(process_result.copy())
        process_result['url'] = ''
        process_result['image'] = ''
        process_result['content'] = ''
        process_result['video'] = ''
    child = child.getnext()

print(article_list)




# print(type(doc('li')))
# items = doc('.list')
# child = items.children()[0]
# while child is not None:
#     print(child)
#     child = child.getnext()

# for item in items.children():
#     print(type(item))
#     print(item.text_content())

#
# del doc
# doc = pq(url="https://cuiqingcai.com")
#
# del doc
# import requests
# doc = pq(requests.get(url="https://cuiqingcai.com").text)
# # print(doc('title').text())
#
# del doc
# doc = pq(html)
# # print(doc('li'))
# print(doc("#container .list li"))
# print(type(doc("#container .list li")))
# items = doc('.list')
# print("\n\n\n")
# print(items)
# lis = items.find('li')
# print(lis)
# del lis
# lis = items.children('.active')
# print("nihaonihao")
# print(lis)
# print(lis.parents())
# del lis
# print("nihaonihao")
# li = doc('.list .item-0.active')
# print(li)
# print(li.siblings())
#
# print("nihaonihao")
# lis = doc('li').items()
# print(type(lis))
# print(type(doc('li').html()))
# print(type(doc('li').text()))
# for item in lis:
#     print(item, type(item))
#     print(item.attr.href)
#     print(type(item.html()))
#     print(item.text())
#
# print("nihaonihao\n")
# print(html)
# li = doc('li:first-child')
# print(li)
# del li
# li = doc('li:last-child')
# print(li)
# del li
# li = doc('li:nth-child(2)')
# print(li)
# del li
# li = doc('li:gt(2)')
# print(li)
# del li
# li = doc('li:nth-child(2n)')
# print(li)
# del li
# li = doc('li:contains(second)')
# print(li)
# del li
# li = doc('.item-0').items()
# print(type(li))
# del li
# li = doc.find('li').items()
# print(li)
# del li
# print("ninininini")
# del doc
# with open('test2.html', encoding='utf-8') as f:
#     content = f.read()
# doc = pq(content)
# print("测试")
# toplist = doc('#toplist')
# print(toplist)
# print("kaishiceshi")
# toplistname1 = toplist('#toplist > div.g-sd3.g-sd3-1 > div > h2:nth-child(1)').text()
# toplistname2 = toplist('.n-minelst > h2:nth-child(3)').text()
# print(toplistname1)
# print(toplistname2)
# lists1 = toplist('.n-minelst > ul:nth-child(2) li.mine').items()
# for item in lists1:
#     result = {
#         'toplist': toplistname1,
#         'id': item.attr('data-res-id'),
#         'name': item('.name > a').text(),
#         'link': 'https://music.163.com' + item('.name > a').attr('href'),
#         'update': item('p.s-fc4').text()
#     }
#     print(result)
#
# lists2 = toplist('.n-minelst > ul:nth-child(4) li.mine').items()
# for item in lists2:
#     result = {
#         'toplist': toplistname2,
#         'id': item.attr('data-res-id'),
#         'name': item('.name > a').text(),
#         'link': 'https://music.163.com' + item('.name > a').attr('href'),
#         'update': item('p.s-fc4').text()
#     }
#     print(result)
#
# song_list_div = doc('#song-list-pre-cache')
# toplist = doc('#toplist > div.g-mn3 > div > div.g-wrap > div > div.cnt > div > div.hd.f-cb > h2').text()
# songs = song_list_div('.m-table > tbody > tr').items()
# for song in songs:
#     result = {
#             'toplist': toplist,
#             'id': song.attr('id'),
#             'songname': song('td:nth-child(2) .ttc b').attr('title'),
#             'song_link': song('td:nth-child(2) .ttc a').attr('href'),
#             'duration': song('span.u-dur').text(),
#             'artist': song('td:nth-child(4) span').attr('title'),
#             'artist-link': song('td:nth-child(4) a').attr('href')
#         }
#     print(result['songname'])
#     print(result)
