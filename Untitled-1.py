def get_prospective_partners():
    partners = []
    while True:
        name = input("Enter the name of a prospective partner (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        partners.append(name)
    return partners

def get_categories():
    categories = []
    for i in range(6):
        category = input(f"Enter category {i+1}: ")
        categories.append(category)
    return categories

def rate_partners(partners, categories):
    ratings = {}
    for partner in partners:
        partner_scores = []
        print(f"\nRating {partner}:")
        for category in categories:
            while True:
                try:
                    score = int(input(f"Rate {partner} on {category} (1-5): "))
                    if score < 1 or score > 5:
                        print("Please enter a score between 1 and 5.")
                    else:
                        partner_scores.append(score)
                        break
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 5.")
        ratings[partner] = partner_scores
    return ratings

def calculate_average_scores(ratings):
    averages = {}
    for partner, scores in ratings.items():
        average_score = sum(scores) / len(scores)
        averages[partner] = average_score
    return averages

def sort_partners(averages):
    sorted_partners = sorted(averages.items(), key=lambda x: x[1], reverse=True)
    return sorted_partners

def print_results(sorted_partners):
    print("\nResults (from highest to lowest):")
    for partner, average in sorted_partners:
        print(f"{partner}: {average:.2f}")

def main():
    print("Welcome to the Personalized Dating Partner Finder!")
    
    # Step 1: Enter prospective partners
    partners = get_prospective_partners()
    
    # Step 2: Enter important categories
    categories = get_categories()
    
    # Step 3: Rate the partners
    ratings = rate_partners(partners, categories)
    
    # Step 4: Calculate average scores
    averages = calculate_average_scores(ratings)
    
    # Step 5: Sort from highest to lowest
    sorted_partners = sort_partners(averages)
    
    # Step 6: Print results
    print_results(sorted_partners)

if __name__ == "__main__":
    main()
