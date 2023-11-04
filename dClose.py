import pandas as pd
from finalclose import close

# a fun that get the intersecton of two freqent item sets and add ther count (support*|D|)
def calculate_intersection_closure_and_count(result_1_data, result_2_data):
    intersection_data = {'Item': [], 'Count': [], 'Closure': []}

    # Create a dictionary to track the union of "Closure" lists for the same items
    closure_dict = {}
    
    for item_1, support_1, closure_1 in zip(result_1_data['Item'], result_1_data['Support'], result_1_data['Closure']):
        for item_2, support_2, closure_2 in zip(result_2_data['Item'], result_2_data['Support'], result_2_data['Closure']):
            # Split items into sets
            set_1 = set(item_1.split(','))
            set_2 = set(item_2.split(','))
            
            # Calculate the intersection of sets
            intersection = set_1.intersection(set_2)
            
            if intersection:
                # Calculate the count of the intersection
                count_intersection = len(intersection)
                
                # Append the intersection and its count to the result
                sorted_intersection = ','.join(sorted(list(intersection)))
                intersection_data['Item'].append(sorted_intersection)
                intersection_data['Count'].append(count_intersection)
                
                # Merge the "Closure" lists for the same items
                if sorted_intersection not in closure_dict:
                    closure_dict[sorted_intersection] = list(closure_1) + list(closure_2)
    
    # Append the merged "Closure" lists to the result
    intersection_data['Closure'] = [closure_dict[item] for item in intersection_data['Item']]

    # Sort the result by 'Item' in ascending order
    sorted_result = sorted(zip(intersection_data['Item'], intersection_data['Count'], intersection_data['Closure']), key=lambda x: x[0])
    intersection_data['Item'], intersection_data['Count'], intersection_data['Closure'] = zip(*sorted_result)

    # Create a DataFrame from the result_intersection dictionary
    df_intersection = pd.DataFrame(intersection_data)

  

    return df_intersection




def dClose(databases,minsup):
    results = {}

    for database in databases:
        print(database)
        # result = close(database,(0.4*len(database) // len(databases)))
        result = close(database,(0.1))

        results[f"result_{databases.index(database) + 1}"] = result


    # frequent items for each sub database
    result_1 = results['result_1']
    result_2 = results['result_2']
    # result_3 = results['result_3']
    print('frequent items for dataset1 and dataset2: ')

    print(result_1)
    print(result_2)
    # print(result_3)

    # the union of all local frequent items
    # print('the uninion :')
    # print(pd.concat([result_1,result_2]))


    gloablFrequent = calculate_intersection_closure_and_count(result_1,result_2)

    print('intersection of c1 and c2:')

    print(gloablFrequent)
    print(pd.DataFrame(gloablFrequent))

    all = pd.concat([pd.DataFrame(gloablFrequent),result_1,result_2])

    print('intersection + union: ')

    print(all)

    # FinalGlobalFrequent = all.loc[all.groupby('Item')['Support'].idxmax()]


    #deleted redondnedt

    max_support = all.groupby('Item')['Count'].transform(max)

    result_df = all[all['Count'] == max_support]

    result_df = result_df.sort_values(by='Item')

    print('Delete diplucate: ie: c_bar=c1 xor c2')

    print(result_df)

    #filter c_bar again by minsup
    print("golbaly frequent items:")
    filtered_items = result_df[result_df['Count'] >= 0.4]

    print(filtered_items)
    # filtered_items = filtered_items.drop('Support', axis=1)
    # filtered_items = filtered_items.drop('Closure', axis=1)

    print('final table: ')
    print(filtered_items)


    return result_1,result_2,filtered_items



print(dClose([d1,d2],0,2))

