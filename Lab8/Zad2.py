positive = "Food was great, they know how to bake fresh bread and excellent pizza. Victoria, the lady who was helping us in the breakfast area was awesome. Location is wonderful, right on the beach, easy access to other attractions from here. I recommend to rent a bike and use their bike trails. They run along the coast and will take you from Gdansk to Sopot, Gdynia. Fun, fun. We had a balcony so on Wednesday and Friday we could hear a life band playing, very nice bonus. This area is super busy, a lot of cars, however they will provide you with a free parking, no problem. Little too hot in the room at the breakfast time , but the food was delicious so it compensated for the inconvenience. Our bathroom's fan didn't work but the bathroom was very large and updated."
negative = "The room was dirty and everything looked old and we soon found animal droppings in the AC unit. My partner has respiratory problems so we went downstairs and informed the front desk receptionist who called in a man. He did not introduce himself and asked us what the problem was so we told him about the animal droppings. He laughed in our faces so we showed him the pictures on our camera. He still laughed so we insisted he come up and see for himself. I asked him who he was and he said he was the owner. We were shocked by his lack of professionalism and bad attitude towards an important matter such as hygiene and safety. When he saw the droppings for himself he offered us a refund of only half of our trip but said that there were no other rooms available. Only when we claimed we would leave a negative review did he offer to refund us all of our money and we quickly left and stayed at the Holiday Inn in Vero Beach instead (which we highly recommend!) Hope this helps steer you towards a better hotel."

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

sentiment_scores = sia.polarity_scores(positive)
print(sentiment_scores)

sentiment_scores = sia.polarity_scores(negative)
print(sentiment_scores)

import text2emotion as te

print(te.get_emotion(positive))
print(te.get_emotion(negative))