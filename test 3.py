""" num2 = 16.95689
print (num2)

num2 = int(round(num2,0))

print (num2)

num2 = float(num2)

print (num2) """


""" n=5
arr=[2, 3, 6, 6, 5, 7, 9, 12]
arr.sort(reverse=True)
print(arr)
print (len(arr))
for i in range(len(arr)-1):
    print(f"{arr[i]} , {arr [i+1]}")
    if arr[i+1] < arr[i]:
        print(f"{arr[i+1]} is the runner up score." )
        break """


# Calculating the number of words in the provided text.

text = """
With over 25 years leading a software business specializing in ERP, Ecommerce, and CRM, I've cultivated a deep understanding of SMEs' unique challenges and opportunities. My journey from a Chartered Accountant to a technology entrepreneur has imbued me with practical business acumen and an appreciation for transformative technologies. Recognizing AI's potential as a paradigm-shifting force, I am now embarking on establishing a Data Science Consultancy tailored for small and medium-sized businesses.

This venture aims to empower SMEs to harness AI for automating processes, optimizing systems, and achieving efficiencies previously deemed unattainable due to economic or resource constraints. However, rather than offering a broad spectrum of services, my focus will be on delivering specialized, high-impact solutions in areas where AI can provide significant value additions and competitive advantage to businesses.

To ensure the technical foundation of this consultancy is robust, I am currently enhancing my skills through a Data Science Bootcamp. Here, I am deepening my understanding of Python for developing customized solutions and gaining proficiency in machine learning models to offer bespoke AI services. Additionally, the bootcamp is a gateway to acquiring the necessary mathematical skills for high-quality, data-driven strategic proposals.

I recognize the importance of building a skilled team to scale operations and meet diverse client needs. As the consultancy gains traction, I will focus on talent acquisition and management, emphasizing creating an agile and adaptive work culture. This approach ensures that we are equipped to handle various projects and continuously evolve our skill set to stay ahead in the dynamic field of data science.

My commitment to this new venture is unwavering. While the bootcamp is a crucial step in this journey, I am equally committed to ongoing learning and staying abreast of the latest developments in AI and data science. With a strategic, focused approach, my consultancy will strive to deliver innovative AI solutions that drive growth and efficiency for SMEs, helping them navigate and thrive in the digital era.
"""

# Counting words
word_count = len(text.split())
print(word_count)