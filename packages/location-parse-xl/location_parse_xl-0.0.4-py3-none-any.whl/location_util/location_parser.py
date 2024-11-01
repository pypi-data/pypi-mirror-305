import re
import collections
from location_util.dictionary_loader import china_location_loader, china_location_change_loader
from collections import defaultdict

class LocationParser(object):

    def __init__(self):
        self.administrative_map_dict = defaultdict(list)
        self.town_village = False
        self.town_village_dict = {}

    def _mapping(self, china_loc, china_change_loc):
        # 整理行政区划码映射表
        self.administrative_map_dict = defaultdict(list)  # 使用字典存储

        for prov in china_loc:
            if prov.startswith('_'):
                continue
            if china_loc[prov]['_alias'] in self.municipalities_cities:
                pass
            else:
                self.administrative_map_dict[china_loc[prov]['_admin_code']].append(
                    [prov, china_loc[prov]['_alias'], None, None, True]
                )

            for city in china_loc[prov]:
                if city.startswith('_'):
                    continue
                for alias_name in china_loc[prov][city]['_alias']:
                    self.administrative_map_dict[china_loc[prov][city]['_admin_code']].append(
                        [prov, city, alias_name, None, True]
                    )

                    for district in china_loc[prov][city]:
                        if district.startswith('_'):
                            continue
                        self.administrative_map_dict[china_loc[prov][city][district]['_admin_code']].append(
                            [prov, city, district,
                             '经济技术开发区' if district.endswith('经济技术开发区') else district,
                             china_loc[prov][city][district]['_alias'], True]
                        )

                        if self.town_village:  # 补充 self.town_village_list
                            key_name = prov + city + district
                            value_dict = china_loc[prov][city][district]
                            self.town_village_dict.update({key_name: value_dict})

        self.old2new_loc_map = {}

        for item in china_change_loc:
            self.administrative_map_dict['000000'].append(
                [item['old_loc'][0], item['old_loc'][1], item['old_loc'][2], False]
            )
            self.old2new_loc_map.update(
                {''.join([i[0] for i in item['old_loc'] if i[0] is not None]): item['new_loc']}
            )

    def _prepare(self):
        self.municipalities_cities = {'北京', '上海', '天津', '重庆', '香港', '澳门'}
        self.loc_alias_string = '【loc_alias】'
        self.exception_suffix_pattern = re.compile('(【loc_alias】(路|大街|街))')

        china_loc = china_location_loader(detail=self.town_village)
        china_change_loc = china_location_change_loader()
        self._mapping(china_loc, china_change_loc)

        self.loc_level_key_list = ['省', '市', '县']
        if self.town_village:
            self.loc_level_key_list.extend(['乡', '村'])
        self.loc_level_key_key_dict = dict(
            [(loc_level, None) for loc_level in self.loc_level_key_list]
        )

    def get_candidates(self, location_text):
        """ 从地址中获取所有可能涉及到的候选地址 """
        candidate_admin_list = []

        # 直接使用字典的方式查找
        for admin_code, admin_items in self.administrative_map_dict.items():
            for item in admin_items:
                for name in item[:3]:  # 只关注前3个元素
                    if isinstance(name, str) and name in location_text:  # 确保 name 是字符串
                        match_info = [location_text.index(name), 0 if name == item[1] else 1]
                        candidate_admin_list.append(item + [1, [match_info]])
                        break

        return candidate_admin_list

    def _process_exception_alias(self, name, location_text):
        location_text = location_text.replace(name, self.loc_alias_string)
        matched_res = self.exception_suffix_pattern.search(location_text)
        return matched_res is None

    def __call__(self, location_text, town_village=False, change2new=True):
        self.town_village = town_village
        if not self.administrative_map_dict:
            self._prepare()
        if self.town_village and not self.town_village_dict:
            self._prepare()

        candidate_admin_list = self.get_candidates(location_text)

        if not candidate_admin_list:
            result = {
                'province': None,
                'city': None,
                'district': None,
                'detail': location_text,
                'full_location': location_text,
                'orig_location': location_text
            }
            if self.town_village:
                result.update({'town': None, 'village': None})

            return self._get_flag_and_result(result)

        # 处理候选地址并生成结果
        final_result = {}
        for candidate in candidate_admin_list:
            prov, city, district, *_, is_valid, match_info = candidate
            final_result['province'] = prov
            final_result['city'] = city
            final_result['district'] = district
            final_result['detail'] = location_text
            final_result['full_location'] = location_text
            final_result['orig_location'] = location_text
            if self.town_village:
                final_result.update({'town': None, 'village': None})

        return self._get_flag_and_result(final_result)

    def _get_final_res(self, final_admin, location_text, county_dup_list,
                       town_village=True, change2new=True):
        result = {
            'province': final_admin[0],
            'city': final_admin[1],
            'district': final_admin[2],
            'detail': location_text,
            'full_location': location_text,
            'orig_location': location_text
        }
        if town_village:
            result.update({'town': None, 'village': None})

        return result

    def _get_flag_and_result(self, result):
        for key in result.keys():
            if result[key] is None:
                result[key] = ''
        return (True, result) if any(result.values()) else (False, result)
