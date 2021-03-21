import requests

class HTTPService:
   def __init__(self, base_url = "http://universities.hipolabs.com", update_endpoint = "/update", search_endpoint = "/search", delete_endpoint = ""):
      self._base_url = base_url
      self._update_endpoint = update_endpoint
      self._search_endpoint = search_endpoint
      self._delete_endpoint = delete_endpoint

   def format_response(self, university):
      return {
         "name": university.get("name", ""),
         "webpage": university.get("web_pages", []),
         "domain": university.get("domains", ""),
         "country": university.get("country", ""),
         "state_province": university.get("state-province", "")
      }

   def format_url(self, name = "", country = ""):
      if not name and not country:
         return ""
   
      include_ampersand = False
      if name and country:
         include_ampersand = True

      query_string = "?"
      
      if name:
         query_string += f"name={name}"

      if include_ampersand:
         query_string += "&"

      if country:
         query_string += f"country={country}"

      return self._base_url + self._search_endpoint + query_string 

   def _update(self):
      requests.get(self._base_url + self._update_endpoint)


   def get_university(self, name = "", country = ""):
      url = self.format_url(name = name, country = country)
      if not url:
         return []

      self._update()
      response = requests.get(url)
      print(url)
      print(response.status_code)
      try:
         response.raise_for_status()
      except requests.exceptions.HTTPError as e:
         print(e)
         return []

      universities = []
      seen = set()
      payload = response.json()
      for university in payload:
         formatted_university = self.format_response(university)
         if formatted_university.get("name") not in seen:
            seen.add(formatted_university.get("name"))
            universities.append(formatted_university)
         
      return universities


class HTTPFactory:
   _http = None

   @staticmethod
   def get_http():
      if not HTTPFactory._http:
         HTTPFactory._http = HTTPService()

      return HTTPFactory._http

if __name__ == "__main__":
   http = HTTPFactory.get_http()
   u1 = http.get_university(name = "stanford university")
   u2 = http.get_university(country = "ghana")
   print(u1)
   print(u2)
      
