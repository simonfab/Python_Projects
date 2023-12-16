#openai

organisationid = "org-w9B7aGchYEW5yLT5ItBosMxR"
organisation_ai_name = "Personal"
secret_key_1 = "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" # simon personal - has no payment details ie not chatgpt acc
secret_key1_name = "simon"

secret_key_2 = "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" #sparkstone api secret key
secret_key = secret_key_2 #assign business one

query = input("enter your question...")

from openai import OpenAI
client = OpenAI(api_key=secret_key)

response = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": query} # + " format as a table"},
    #{"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    #{"role": "user", "content": "Where was it played?"}
  ]
)
print (response.choices[0])


# print("Here is a table listing the winners of the last 10 FIFA World Cups:\n\n| Year | Winner       | Runner-up            |\n|------|--------------|----------------------|\n| 2018 | France       | Croatia              |\n| 2014 | Germany      | Argentina            |\n| 2010 | Spain        | Netherlands          |\n| 2006 | Italy        | France               |\n| 2002 | Brazil       | Germany              |\n| 1998 | France       | Brazil               |\n| 1994 | Brazil       | Italy                |\n| 1990 | West Germany | Argentina            |\n| 1986 | Argentina    | West Germany         |\n| 1982 | Italy        | West Germany         |\n\nNote: The FIFA World Cup takes place every four years, so the years provided for each tournament refer to the starting year of the event.', role='assistant', function_call=None, tool_calls=None")