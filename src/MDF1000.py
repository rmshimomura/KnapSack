import os
import time
import random


def clear():
    if os.name == 'nt':
        _ = os.system('cls')


number_of_elements = int(input("How many elements? : "))
create_limit = open("superiorLimit" + str(number_of_elements) + "elements.txt", "w")
create_exhaust = open("exhaust" + str(number_of_elements) + "elements.txt", "a")
results_file_limit = open("superiorLimit" + str(number_of_elements) + "elements.txt", "a")
results_file_exhaust = open("exhaust" + str(number_of_elements) + "elements.txt", "a")

for x in range(10):
  data = []
  graph = []
  maximum_interest = 0
  max_int_numbers = []
  a = False

  # Collecting data for the Algorithm

  for i in range(number_of_elements):
      temp = []
      weight = random.randint(10,100)
      temp.append(weight)
      interest = random.randint(10,100)
      temp.append(interest)
      temp.append(f"[{i + 1}]")
      data.append(temp)
  clear()

  capacity = 0

  for w in range(number_of_elements):
    capacity += data[w][0]

  capacity = capacity//2
  maximum_capacity = capacity

  # Ordering by interest/weight

  data.sort(key=lambda x: x[1]/x[0], reverse=True)
  results_file_limit.write(f"Superior Limit\nCapacity = {capacity}\n\n")
  results_file_limit.write(f"Data sorted in ")

  for i in range(len(data)):
      results_file_limit.write(f"{data[i][2]} ")

  results_file_limit.write("because of interest/weight \n\n")
  results_file_limit.write(f"data = {data}\n")

  # Building first branch

  while(1):

      temp = []
      temporary_capacity = 0
      for j in range(len(data)):
          temp.append(maximum_capacity//data[j][0])
          maximum_interest += maximum_capacity//data[j][0] * data[j][1]
          temporary_capacity += maximum_capacity//data[j][0] * data[j][0]
          maximum_capacity -= maximum_capacity//data[j][0] * data[j][0]
      graph.append(temp)
      max_int_numbers = graph[0]

      break

  backup = graph.copy()

  # Checking for new possibilities
  start_limit = time.time()
  while(graph[0][0] > 0):

      if a:
          break

      # This goes backwards on the branch
      for i in range(len(graph[0]) - 2, -1, -1):

          maximum_capacity = capacity  # Reset every time
          interest = 0  # Reset every new branch to see if interest > maximumInterest
          temporary_capacity = 0
          limitant = 0

          # Found a place starting from penultimate position that can be reduced 1 unity
          if(graph[0][i] != 0):

              temp = graph[0].copy()  # Copy graph to a temporary one
              temp[i] -= 1  # Reduce 1 unity for new branch

              if(time.time() - start_limit > 3600):
                  results_file_limit.write(f"Process reached time limit of 2 hours obtaining {max_int_numbers} with maximum interest of {maximum_interest} as best solution\n")
                  a = True
                  break

              # From first position to position that was modified on the upper line ^, reduce the capacity and the interest
              for k in range(0, i + 1):

                  maximum_capacity -= temp[k] * data[k][0]
                  temporary_capacity += temp[k] * data[k][0]
                  interest += temp[k] * data[k][1]

                  if(time.time() - start_limit > 3600):
                      results_file_limit.write(f"Process reached time limit of 2 hours obtaining {max_int_numbers} with maximum interest of {maximum_interest} as best solution\n")
                      a = True
                      break

              limitant = interest + (temp[i] * data[i][1]) + ((data[i+1][1]/data[i+1][0]) * (capacity - (temporary_capacity + data[i][0]*temp[i])))

              if limitant < maximum_interest:
                  temp[i] = 0
                  graph[0] = temp
                  continue

              if(time.time() - start_limit > 3600):
                  results_file_limit.write(f"Process reached time limit of 2 hours obtaining {max_int_numbers} with maximum interest of {maximum_interest} as best solution\n")
                  a = True
                  break

              # Now modifiy the capacity and interest with new values
              for j in range(i + 1, len(temp)):

                  temp[j] = (maximum_capacity//data[j][0])
                  interest += temp[j] * data[j][1]
                  temporary_capacity += maximum_capacity//data[j][0] * data[j][0]
                  maximum_capacity -= maximum_capacity//data[j][0] * data[j][0]

                  if(time.time() - start_limit > 3600):
                      results_file_limit.write(f"Process reached time limit of 2 hours obtaining {max_int_numbers} with maximum interest of {maximum_interest} as best solution\n")
                      a = True
                      break

              if(interest > maximum_interest):
                  maximum_interest = interest
                  max_int_numbers = temp.copy()

              graph[0] = temp  # For the while loop
              # Sorting for writing on file
              graph.sort(key=lambda x: x[number_of_elements - 1])

              break

  end_limit = time.time()

  print("===============\nLIMIT\n")
  if not a:
      results_file_limit.write(f"Maximum interest = {maximum_interest}\nMaximum interest numbers = {max_int_numbers}\n")
      print(f"Maximum interest = {maximum_interest}\n")
      results_file_limit.write(f"Time spent = {end_limit - start_limit} seconds \n")
      results_file_limit.write("\n\n\n\=======================================\n\n\n")
  else:
      print(f"Maximum interest = {maximum_interest}\n")
      results_file_limit.write(f"Time spent = {end_limit - start_limit} seconds \n")
      print("Process interrupted.\n")
      results_file_limit.write("\n\n\n\=======================================\n\n\n")

  # exhaust

  maximum_capacity = capacity
  maximum_interest = 0
  max_int_numbers = []
  graph = backup.copy()
  a = False

  results_file_exhaust.write(f"Exhaust\nCapacity = {capacity}\n\n")
  results_file_exhaust.write(f"Data sorted in ")

  for i in range(len(data)):
      results_file_exhaust.write(f"{data[i][2]} ")
  results_file_exhaust.write("because of interest/weight \n\n")
  results_file_exhaust.write(f"data = {data}\n")

  while(1):

      temp = []
      temporary_capacity = 0
      for j in range(len(data)):
          temp.append(maximum_capacity//data[j][0])
          maximum_interest += maximum_capacity//data[j][0] * data[j][1]
          temporary_capacity += maximum_capacity//data[j][0] * data[j][0]
          maximum_capacity -= maximum_capacity//data[j][0] * data[j][0]
      graph.append(temp)
      max_int_numbers = graph[0]

      break

  start_exhaust = time.time()

  while(graph[0][0] > 0):

      if a:
          break

      # This goes backwards on the branch
      for i in range(len(graph[0]) - 2, -1, -1):

          maximum_capacity = capacity
          interest = 0
          temporary_capacity = 0

          if(graph[0][i] != 0):

              temp = graph[0].copy()
              temp[i] -= 1

              if(time.time() - start_exhaust > 3600):
                  results_file_exhaust.write(f"Process reached time limit of 2 hours obtaining {max_int_numbers} with maximum interest of {maximum_interest} as best solution")
                  a = True
                  break

              for k in range(0, i + 1):

                  maximum_capacity -= temp[k] * data[k][0]
                  temporary_capacity += temp[k] * data[k][0]
                  interest += temp[k] * data[k][1]

                  if(time.time() - start_exhaust > 3600):
                      results_file_exhaust.write(f"Process reached time limit of 2 hours obtaining {max_int_numbers} with maximum interest of {maximum_interest} as best solution")
                      a = True
                      break

              for j in range(i + 1, len(temp)):

                  temp[j] = (maximum_capacity//data[j][0])
                  interest += temp[j] * data[j][1]
                  temporary_capacity += maximum_capacity//data[j][0] * data[j][0]
                  maximum_capacity -= maximum_capacity//data[j][0] * data[j][0]

                  if(time.time() - start_exhaust > 3600):
                      results_file_exhaust.write(f"Process reached time limit of 2 hours obtaining {max_int_numbers} with maximum interest of {maximum_interest} as best solution")
                      a = True
                      break

              if(interest > maximum_interest):
                  maximum_interest = interest
                  max_int_numbers = temp.copy()

              graph[0] = temp
              graph.sort(key=lambda x: x[number_of_elements - 1])

              break
  end_exhaust = time.time()

  print("===============\nExhaust\n")
  if not a:
      results_file_exhaust.write(f"Maximum interest = {maximum_interest}\nMaximum interest numbers = {max_int_numbers}\n")
      results_file_exhaust.write(f"Time spent = {end_exhaust - start_exhaust} seconds \n")
      print(f"Maximum interest = {maximum_interest}\n")
      results_file_exhaust.write("\n\n\n\=======================================\n\n\n")
  else:
      print(f"Maximum interest = {maximum_interest}\n")
      print("Process interrupted.")
      results_file_exhaust.write("\n\n\n\=======================================\n\n\n")
