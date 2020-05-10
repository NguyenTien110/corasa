import requests

fetch_url = 'https://corona-api.kompa.ai/graphql'
totalVietNam = """query totalVietNam {
  totalVietNam {
    confirmed
    deaths
    recovered
    __typename
  }
}"""

totalConfirmed = """query totalConfirmed {
  totalConfirmed
  totalConfirmedLast
  trendlineGlobalCases {
    date
    confirmed
    __typename
  }
}"""

totalRecovered = """query countries {
  totalRecovered  provinces {
    Confirmed
    Deaths
    Recovered
    __typename
  }
  totalRecoveredLast
  trendlineGlobalCases {
    date
    recovered
    __typename
  }
}"""

totalDeaths = """query countries {
  totalDeaths
  provinces {
    Confirmed
    Deaths
    Recovered
    __typename
  }
  totalDeathsLast
  trendlineGlobalCases {
    date
    death
    __typename
  }
}"""

provinces_VietNam_status = """query provinces {
  provinces {
    Province_Name
    Province_Id
    Lat
    Long
    Confirmed
    Deaths
    Recovered
    Last_Update
    __typename
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
        __typename
        }
}"""

headers = {"Content-Type": "application/json", "origin": "https://corona.kompa.ai"}


def run_query(query):  # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post(fetch_url, json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()['data']
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


# result = run_query(totalVietNam)
# result = run_query(totalConfirmed)
# result = run_query(totalRecovered)
# result = run_query(totalDeaths)
# result = run_query(provinces_VietNam_status)
# result = run_query(global_status)
# print(result)
