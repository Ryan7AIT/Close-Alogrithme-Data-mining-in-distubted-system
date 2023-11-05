import pandas as pd
import math

def close(dataset,minsup):


# d = data.iloc[:, 0:2]
# d['Item']=data['Item'].str.strip().str.lower() +  ','
# a = d.groupby(['Transaction'])


# dataset = [ i.strip().split(',')[:-1] for i in a.sum().iloc[:,0]]

    def calculate_support(dataset, item):
        item = item.split(',')  # Split the input string into a list

        count = 0
        for transaction in dataset:
            if all(i in transaction for i in item):
                count += 1

        support = count / len(dataset)
        return support
    

    def calculate_Count(dataset, item):
        item = item.split(',')  # Split the input string into a list

        count = 0
        for transaction in dataset:
            if all(i in transaction for i in item):
                count += 1

        return count


    def filter_items_by_minsup(results_df, minsup):

        filtered_items = results_df[results_df['Support'] >= minsup]
        item_list = filtered_items['Item'].tolist()
        return item_list,filtered_items


    def generate_candidate_itemsets(frequent_itemsets_k):
        candidate_itemsets_k_plus_1 = []

        for i in range(len(frequent_itemsets_k)):
            for j in range(i + 1, len(frequent_itemsets_k)):
                itemset1 = frequent_itemsets_k[i].split(',')
                itemset2 = frequent_itemsets_k[j].split(',')
                
                # Check if the first k-1 elements are the same to join the itemsets.
                if itemset1[:-1] == itemset2[:-1]:
                    # Create a new candidate (k+1)-itemset by joining the two k-itemsets.
                    new_itemset = ','.join(sorted(set(itemset1 + itemset2)))
                    candidate_itemsets_k_plus_1.append(new_itemset)

        return candidate_itemsets_k_plus_1


    def create_dict_from_dataframe(d):
        item_closure_dict = dict(zip(d['Item'], d['Closure']))
        return item_closure_dict




    def get_closure(item, dataset):
        item = item.split(',')  # Split the input string into a list of items

        matching_lists = [data_list for data_list in dataset if all(i in data_list for i in item)]
        
        if len(matching_lists) == 0:
            return []

        intersection = sorted(set(matching_lists[0]).intersection(*matching_lists[1:]))
        return intersection



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


    def filter_items(d, l):
        result = []

        for item in l:
            elements = item.split(',')
            is_item_valid = True
            for value in d.values():
                if all(element in ''.join(value) for element in elements):
                    is_item_valid = False
                    break
            if is_item_valid:
                result.append(item)

        return result


    def extract_association_rules(df, filtered_item_list):
        association_rules = []
        for index, row in df.iterrows():
            item = row['Item']
            closure = row['Closure']
            if closure != item and item in filtered_item_list and calculate_support(dataset,item) !=0:
                cleaned_closure = ''.join(char for char in closure if char not in item.replace(',', ''))
                # cleaned_closure = ''.join(char for char in ''.join(closure).replace(',', '') if char not in item.replace(',', ''))

                association_rule = f"{item} -> {cleaned_closure}"
                association_rules.append(association_rule)
        return association_rules





    allitems = [item for sublist in dataset for item in sublist]

    candidate  = sorted(set(allitems))
    itteration=0
    #result table
    results = pd.DataFrame(columns=['Item', 'Support'])
    frequent_items = []
    assoc_rule_list=[]


    returnValue = pd.DataFrame(columns=['Item', 'Support'])



    while len(candidate ) > 0 :

        # print('------------------------------------------')
        # print('itiration ')
        # print(itteration+1)
        # print(candidate)

        itteration = itteration+1
        # Create an empty list to store the results
        results = []

        # Calculate and store the support for each item in the candidate list
        for item in candidate:
            support = calculate_support(dataset, item) 
            count = calculate_Count(dataset, item) 

            closure = get_closure(item, dataset)
            results.append({'Item': item, 'Support': support,'Closure': closure, 'Count': count})

        # Create a DataFrame from the list of dictionaries
        results_df = pd.DataFrame(results)
        results_df = results_df.sort_values(by='Support', ascending=False)




        filtered_item_list,filtered_items = filter_items_by_minsup(results_df, minsup)
       

        if(itteration==1) :
     
            frequent_items.append(filtered_item_list)
            returnValue = pd.concat([returnValue,filtered_items], ignore_index=True)

        if(itteration>1):
            frequent_items.append(filtered_item_list)
            returnValue = pd.concat([returnValue,filtered_items], ignore_index=True)
            

      


        next_candidate = generate_candidate_itemsets(filtered_item_list)

        next_candidate = [s.lstrip(',').lstrip(',') for s in next_candidate]


  


        closures = create_dict_from_dataframe(filtered_items)

        # print(closures)


        # filtered_list = filter_list_with_dict_containment(next_candidate, closures)
        filtered_list = filter_items(closures,next_candidate )



        candidate = filtered_list   

        assoc_rule_list.append(extract_association_rules(results_df,filtered_item_list))

    rules_list = [item for sublist in assoc_rule_list for item in sublist]


    # Create a DataFrame with 'Rule' column
    df_rules = pd.DataFrame({'Rule': rules_list})


    # ###################################################################################################3
    # def confiance(rule_part1,rule_part2):
    #     calculate_support(dataset,(rule_part1 + rule_part2))/calculate_support(dataset,rule_part1)
    def calculate_confidence_from_rule(rule):
        rule_parts = rule.split(' -> ')
        rule_part1, rule_part2 = rule_parts[0], rule_parts[1]
        support_rule1_and_rule2 = calculate_support(dataset, (rule_part1 +','+ rule_part2))
        support_rule1 = calculate_support(dataset, rule_part1)
        confidence = support_rule1_and_rule2 / support_rule1
        return confidence
    # def lift(rule_part1,rule_part2):
    #     calculate_support(dataset,(rule_part1 + rule_part2))/(calculate_support(dataset,rule_part1)*calculate_support(dataset,rule_part2))
    def calculate_lift_from_rule(rule):
        rule_parts = rule.split(' -> ')
        rule_part1, rule_part2 = rule_parts[0], rule_parts[1]
        support_rule1_and_rule2 = calculate_support(dataset, (rule_part1 +','+ rule_part2))
        support_rule1 = calculate_support(dataset, rule_part1)
        support_rule2 = calculate_support(dataset, rule_part2)
        if (support_rule1 * support_rule2)==0:
            lift_value = 0
        else :
            lift_value = support_rule1_and_rule2 /((support_rule1 * support_rule2*1.07))
        return lift_value

    # df_rules['Confidence'] = df_rules['Rule'].apply(lambda x: confiance(x.split(' -> ')[0],x.split(' -> ')[1]))
    df_rules['Confidence'] = df_rules['Rule'].apply(calculate_confidence_from_rule)

    # df_rules['Lift'] = df_rules['Rule'].apply(lambda x: lift(x.split(' -> ')[0],x.split(' -> ')[1]))
    df_rules['Lift'] = df_rules['Rule'].apply(calculate_lift_from_rule)

    # Output the DataFrame

    print(returnValue)


    return returnValue


dataset = [['A', 'B', 'C', 'D', 'E'],
           ['A', 'B'],
           ['C', 'E'],
           ['A', 'B', 'D', 'E'],
           ['A', 'C', 'D']]
    

close(dataset,0.4)
