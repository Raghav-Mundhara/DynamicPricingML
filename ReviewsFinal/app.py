# import pandas as pd
# import random

# # Define the lists of possible values for each column
# services = ['app', 'website', 'figma', 'frontend', 'backend', 'docs', 'ppt']
# client_emails = ['raghav@gmail.com', 'kaushik@gmail.com', 'test@gmail.com', 'anushka@gmail.com', 'nishtha@gmail.com']
# freelancer_emails = ['raghav@gmail.com', 'kaushik@gmail.com', 'test@gmail.com', 'anushka@gmail.com', 'nishtha@gmail.com']

# # Sample review templates
# positive_review_templates = [
#     "I'm very satisfied with the {service} created by {freelancer_email}. Excellent work!",
#     "The {service} developed by {freelancer_email} exceeded my expectations. Highly recommended!",
#     "The {service} provided by {freelancer_email} was professional and efficient. Thank you!",
#     "I appreciate the effort put into the {service} project by {freelancer_email}. Well done!",
#     "The {service} work done by {freelancer_email} was exceptional. I'm impressed!",
#     "{service} created by {freelancer_email} is exactly what I wanted. Great job!",
#     "I'm extremely satisfied with the {service} developed by {freelancer_email}. Thank you so much!",
#     "The {service} provided by {freelancer_email} was top-notch. I'm very happy with the result.",
#     "I'm delighted with the {service} project delivered by {freelancer_email}. It's perfect!",
#     "The {service} work done by {freelancer_email} surpassed my expectations. Highly impressed!",
# ]

# negative_review_templates = [
#     "Unfortunately, the {service} provided by {freelancer_email} did not meet my expectations. Disappointed.",
#     "The {service} developed by {freelancer_email} had several issues and was delivered late. Not recommended.",
#     "I'm dissatisfied with the {service} project. Communication with {freelancer_email} was poor.",
#     "The {service} work done by {freelancer_email} was subpar. I regret hiring them for this project.",
#     "The {service} provided by {freelancer_email} was not up to standard. I won't be working with them again.",
#     "I'm unhappy with the {service} created by {freelancer_email}. It wasn't what I expected.",
#     "I'm extremely disappointed with the {service} created by {freelancer_email}. It's not usable at all.",
#     "{freelancer_email} failed to deliver a satisfactory {service} project. It was a waste of time and money.",
#     "I'm regretting hiring {freelancer_email} for the {service} project. The quality of work was poor.",
#     "The {service} provided by {freelancer_email} was a complete disaster. I wouldn't recommend them to anyone.",
# ]

# neutral_review_templates = [
#     "The {service} provided by {freelancer_email} was satisfactory. It met my requirements.",
#     "I'm neutral about the {service} project delivered by {freelancer_email}. It was neither exceptional nor disappointing.",
#     "The {service} work done by {freelancer_email} was average. It could have been better.",
#     "{freelancer_email} provided an okay {service} project. It was neither good nor bad.",
#     "The {service} created by {freelancer_email} was decent. It served its purpose adequately.",
#     "The {service} developed by {freelancer_email} was acceptable. It met the basic requirements.",
#     "I have mixed feelings about the {service} project provided by {freelancer_email}. It was neither great nor terrible.",
#     "The {service} work done by {freelancer_email} was okay. It didn't exceed expectations, but it wasn't terrible either.",
#     "The {service} provided by {freelancer_email} was satisfactory. It wasn't exceptional, but it got the job done.",
#     "I'm indifferent about the {service} project provided by {freelancer_email}. It neither impressed nor disappointed me.",
# ]

# # Generate random data for the dataset
# def generate_data(num_rows):
#     data = []
#     for _ in range(num_rows):
#         client_email = random.choice(client_emails)
#         freelancer_email = random.choice(freelancer_emails)
#         service = random.choice(services)
#         project_name = f"Project {_}"
        
#         # Randomly select the review template based on the sentiment
#         sentiment_choice = random.random()
#         if sentiment_choice < 0.3:
#             review_template = random.choice(neutral_review_templates)
#         elif sentiment_choice < 0.7:
#             review_template = random.choice(positive_review_templates)
#         else:
#             review_template = random.choice(negative_review_templates)
            
#         # Generate the review
#         review = review_template.format(service=service, freelancer_email=freelancer_email)
#         data.append([client_email, freelancer_email, service, project_name, review])
#     return data

# # Generate the dataset
# num_rows = 1000  # Change this to the desired number of rows
# data = generate_data(num_rows)

# # Create a DataFrame from the generated data
# df = pd.DataFrame(data, columns=['client_email', 'freelancer_email', 'service', 'project_name', 'review'])

# # Modify sentiment assignment based on keywords
# def assign_sentiment(review):
#     positive_keywords = ['satisfied', 'exceeded', 'recommended', 'professional', 'efficient', 'great', 'impressed', 'perfect', 'exceptional']
#     negative_keywords = ['disappointed', 'issues', 'late', 'poor', 'subpar', 'regret', 'waste', 'disaster', 'failed', 'disaster',"won't","unhappy","unfortunately"]
#     neutral_keywords = ['satisfactory', 'average', 'okay', 'decent', 'acceptable']

#     if any(word in review for word in positive_keywords):
#         return 'Positive'
#     elif any(word in review for word in negative_keywords):
#         return 'Negative'
#     elif any(word in review for word in neutral_keywords):
#         return 'Neutral'
#     else:
#         return 'Neutral'  # Default to neutral if sentiment cannot be determined

# # Apply sentiment analysis to the reviews
# df['sentiment'] = df['review'].apply(assign_sentiment)

# # Save the dataset to a CSV file
# df.to_csv('data.csv', index=False)

# print("Dataset generated and saved to 'data.csv'")


from textblob import TextBlob
texts=["I'm very satisfied with the app created by freelancer_email. Excellent work!",
    "The website developed by freelancer_email exceeded my expectations. Highly recommended!",
    "The figma provided by freelancer_email was professional and efficient. Thank you!",
    "I appreciate the effort put into the frontend project by freelancer_email. Well done!",
    "The backend work done by freelancer_email was exceptional. I'm impressed!",
    "docs created by freelancer_email is exactly what I wanted. Great job!",
    "I'm extremely satisfied with the ppt developed by freelancer_email. Thank you so much!",
    "The app provided by freelancer_email was top-notch. I'm very happy with the result.",
    "Unfortunately, the website provided by freelancer_email did not meet my expectations. Disappointed.",
    "The figma developed by freelancer_email had several issues and was delivered late. Not recommended.",
    "I'm dissatisfied with the frontend project. Communication with freelancer_email was poor.",
    "The backend work done by freelancer_email was subpar. I regret hiring them for this project.",
    "The docs provided by freelancer_email was not up to standard. I won't be working with them again.",
    "I'm unhappy with the ppt created by freelancer_email. It wasn't what I expected.",

    ]

for text in texts:
    print(text)
    blob = TextBlob(text)
    print(blob.sentiment)
    print("\n")