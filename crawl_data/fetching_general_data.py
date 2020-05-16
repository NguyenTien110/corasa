import requests

fetch_url = 'https://corona-api.kompa.ai/graphql'
vietnam_status = """query totalVietNam {
  totalVietNam {
    confirmed
    deaths
    recovered
  }
}"""

confirm_global = """query totalConfirmed {
  totalConfirmed
  totalConfirmedLast
  trendlineGlobalCases {
    date
    confirmed
  }
}"""

resolve_global = """query countries {
  totalRecovered  provinces {
    Confirmed
    Deaths
    Recovered
  }
  totalRecoveredLast
  trendlineGlobalCases {
    date
    recovered
  }
}"""

death_global = """query countries {
  totalDeaths
  provinces {
    Confirmed
    Deaths
    Recovered
  }
  totalDeathsLast
  trendlineGlobalCases {
    date
    death
  }
}"""

provinces_vietnam_status = """query provinces {
  provinces {
    Province_Name
    Province_Id
    Lat
    Long
    Confirmed
    Deaths
    Recovered
    Last_Update
  }
}"""

global_status = """query countries {
    globalCasesToday {
        country
        totalCase
        totalDeaths
        totalRecovered
        longitude
        latitude
        }
}"""

headers = {"Content-Type": "application/json", "origin": "https://corona.kompa.ai"}


def run_query(query):  # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post(fetch_url, json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()['data']
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


# result = run_query(vietnam_status)['totalVietNam']
# result = run_query(totalConfirmed)
# result = run_query(totalRecovered)
# result = run_query(totalDeaths)
# result = run_query(provinces_VietNam_status)
# result = run_query(global_status)
# print(result['confirmed'])
