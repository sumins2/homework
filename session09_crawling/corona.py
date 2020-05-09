def extract_info(corona_list):
  result = []
  for corona in corona_list:
    info = corona.contents

    corona_info = {
      'city' : info[1].string,
      'city_detail' : info[2].string,
      'name' : info[3].text,
      'phone' : info[4].string
    }

    result.append(corona_info)
    
  return result