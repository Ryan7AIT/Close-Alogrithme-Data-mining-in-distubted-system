import pandas as pd

dataset = [['A', 'B', 'C', 'D', 'E'],
           ['A', 'B'],
           ['C', 'E'],
           ['A', 'B', 'D', 'E'],
           ['A', 'C', 'D']]

dataset1 = [['coffee', 'tea', 'bread', 'limonad'],
           ['coffee', 'tea'],
           ['bread', 'cola'],
           ['coffee', 'tea', 'limonad', 'cola'],
           ['coffee', 'bread', 'limonad']]

def calculate_support(dataset, item):

    support_count = 0
    for transaction in dataset:
        if set(item).issubset(set(transaction)):
            support_count += 1
    support = support_count / len(dataset)

    return support


def filter_items_by_minsup(results_df, minsup):

    filtered_items = results_df[results_df['Support'] >= minsup]
    item_list = filtered_items['Item'].tolist()
    return item_list,filtered_items


def get_closure(item,dataset):
    target_items = list(item)
    matching_lists = [data_list for data_list in dataset if all(item in data_list for item in target_items)]

    intersection = sorted(set(matching_lists[0]).intersection(*matching_lists[1:]))
    return ''.join(intersection)


#this get all the closures in a dict


def create_dict_from_dataframe(d):
    item_closure_dict = dict(zip(d['Item'], d['Closure']))
    return item_closure_dict



def generate_candidate_itemsets(frequent_itemsets_k):

    candidate_itemsets_k_plus_1 = []

    for i in range(len(frequent_itemsets_k)):
        for j in range(i + 1, len(frequent_itemsets_k)):
            # Check if the first k-1 items are the same to join the itemsets.
            if frequent_itemsets_k[i][:-1] == frequent_itemsets_k[j][:-1]:
                # Create a new candidate (k+1)-itemset by joining the two k-itemsets.
                new_itemset = ''.join(sorted(set(frequent_itemsets_k[i] + frequent_itemsets_k[j])))
                candidate_itemsets_k_plus_1.append(new_itemset)


    return candidate_itemsets_k_plus_1



#!!!! to change

def filter_list_with_dict(input_list, item_closure_dict):
    filtered_list = []
    for item in input_list:
        found = False
        for char in item:
            if char in item_closure_dict and item_closure_dict[char] == item:
                found = True
                break
        if not found:
            filtered_list.append(item)
    return filtered_list

def filter_list_with_dict_containment(input_list, item_closure_dict):
    filtered_list = []
    for item in input_list:
        found = False
        for key, value in item_closure_dict.items():
            if item in value:
                found = True
                break
        if not found:
            filtered_list.append(item)
    return filtered_list





def extract_association_rules(df, filtered_item_list):
    association_rules = []
    for index, row in df.iterrows():
        item = row['Item']
        closure = row['Closure']
        if closure != item and item in filtered_item_list:
            cleaned_closure = ''.join(char for char in closure if char not in item)
            association_rule = f"{item} -> {cleaned_closure}"
            association_rules.append(association_rule)
    return association_rules



# ###################################################################################################3
# def confiance(rule_part1,rule_part2):
#     calculate_support(dataset,(rule_part1 + rule_part2))/calculate_support(dataset,rule_part1)
def calculate_confidence_from_rule(rule,dataset):
    rule_parts = rule.split(' -> ')
    rule_part1, rule_part2 = rule_parts[0], rule_parts[1]
    support_rule1_and_rule2 = calculate_support(dataset, (rule_part1 + rule_part2))
    support_rule1 = calculate_support(dataset, rule_part1)
    confidence = support_rule1_and_rule2 / support_rule1
    return confidence
# def lift(rule_part1,rule_part2):
#     calculate_support(dataset,(rule_part1 + rule_part2))/(calculate_support(dataset,rule_part1)*calculate_support(dataset,rule_part2))
def calculate_lift_from_rule(rule,dataset):
    rule_parts = rule.split(' -> ')
    rule_part1, rule_part2 = rule_parts[0], rule_parts[1]
    support_rule1_and_rule2 = calculate_support(dataset, (rule_part1 + rule_part2))
    support_rule1 = calculate_support(dataset, rule_part1)
    support_rule2 = calculate_support(dataset, rule_part2)
    lift_value = support_rule1_and_rule2 / (support_rule1 * support_rule2)
    return lift_value



def close(dataset,minsup):
    


    #debut
    #1
    allitems = [item for sublist in dataset for item in sublist]

    candidate  = sorted(set(allitems))
    itteration=0
    #result table
    results = pd.DataFrame(columns=['Item', 'Support'])
    frequent_items = []
    assoc_rule_list=[]

    while len(candidate ) > 0 :
        print('------------------------------------------')
        print('itiration ')
        print(itteration+1)
        # print(candidate)

        itteration = itteration+1
        # Create an empty list to store the results
        results = []

        # Calculate and store the support for each item in the candidate list
        for item in candidate:
            support = calculate_support(dataset, item) 
            closure = get_closure(item, dataset)
            results.append({'Item': item, 'Support': support, 'Closure': closure})

        # Create a DataFrame from the list of dictionaries
        results_df = pd.DataFrame(results)
        results_df = results_df.sort_values(by='Support', ascending=False)


        print(results_df)


        filtered_item_list,filtered_items = filter_items_by_minsup(results_df, minsup)
        print('after min sup puring: ie: les frequent item pour cette itteration:')
        print(filtered_item_list)

        if(itteration==1) :
            print('for i1')
            print(filtered_item_list)
            frequent_items.append(filtered_item_list)
        if(itteration>1):
            frequent_items.append(filtered_item_list)


        print('les candidat retenu:')
        print(filtered_item_list)

    


        # print(filtered_item_list)
        # print('suprimier les item par a port a minsup')
        # print(filtered_items)


        # Create the dictionary of rules from the data frame with all the values with suport>minsum
        # rules = {}

        # for index, row in filtered_items.iterrows():
        #     if row['Support'] > 0.4:
        #         key = row['Item']
        #         value = row['Closure'].replace(row['Item'], '')
        #         rules[key] = value

        # print('les regle dassociation')
        # print(rules)






        #filtered_items = a table with all frequent items
        #filtered_item_list = a list with all frequent items


        #next iteration candidate

        next_candidate = generate_candidate_itemsets(filtered_item_list)


        print('les candidat pour letration suivante:')

        print(next_candidate)


        closures = create_dict_from_dataframe(filtered_items)

        # print(closures)


        filtered_list = filter_list_with_dict_containment(next_candidate, closures)
        # print(closures,next_candidate)
        print('elaguer ces candidat en utilisant les fermutures: ')
        print(filtered_list)

        candidate = filtered_list



        if(len(candidate) ==0):
            print('les items set frequent sont:')
            flattened_list = [item for sublist in frequent_items for item in sublist]
            print(flattened_list)
        # break

        assoc_rule_list.append(extract_association_rules(results_df,filtered_item_list))





    #  Create the dictionary of rules from the data frame with all the values with suport>minsum
    #     rules = {}

    # for index, row in filtered_items.iterrows():
    #     if row['Support'] > 0.4:
    #         key = row['Item']
    #         value = row['Closure'].replace(row['Item'], '')
    #         rules[key] = value

    # print('les regle dassociation')
    # print(rules)
    # print(assoc_rule_list)


    rules_list = [item for sublist in assoc_rule_list for item in sublist]

    # Create a DataFrame with 'Rule' column
    df_rules = pd.DataFrame({'Rule': rules_list})




    # df_rules['Confidence'] = df_rules['Rule'].apply(lambda x: confiance(x.split(' -> ')[0],x.split(' -> ')[1]))
    # df_rules['Confidence'] = df_rules['Rule'].apply(calculate_confidence_from_rule)
    df_rules['Confidence'] = df_rules.apply(lambda row: calculate_confidence_from_rule(row['Rule'], dataset), axis=1)


    # df_rules['Lift'] = df_rules['Rule'].apply(lambda x: lift(x.split(' -> ')[0],x.split(' -> ')[1]))
    # df_rules['Lift'] = df_rules['Rule'].apply(calculate_lift_from_rule)
    df_rules['Lift'] = df_rules.apply(lambda row: calculate_lift_from_rule(row['Rule'], dataset), axis=1)



    # Output the DataFrame
    print(df_rules)

    return df_rules

