`strl` holds list like data at disk storage file insted of memory.

## Purpoces

By using disk storage, there is following advantages.

- reduce memory usage
- store the data after exit
- easy to handle compared to sql

Disk storage used to be very slow, but now it's getting fast enough due to the popularization of SSD. Especially in cloud servers, the cost increases in reflection of memory amount. In order to save cost, reduce memory usage is key factor.
In addition, this package is convenient as simple storage substitute for sql. Sometimes you just want to save single piece of data, sometimes sql is cumbersome for study or test. Thies package is very easy to use.


## Sample usage(create file)

```python
import strl

#mode w creates "people" file in "__stlist__" folder
ppl = strl.STRL("people",mode="w")


ppl.append({"name":"bob","age":21})

people = [
  {"name":"tom","age":51},
  {"name":"linda","age":19},
  ]

ppl.append_list_items(people)


#
# return data
#
for item in ppl:
  print(item["name"]) #bob,tom,linda

print(ppl.get_item(1)) #{'name': 'tom', 'age': 51}
print(ppl.get_list()) # [{'name': 'bob', 'age': 21}, {'name': 'tom', 'age': 51}, {'name': 'linda', 'age': 19}]

filtered = ppl.get_filtered_list(lambda x: True if x["age"] <= 30 else False)
print(filtered) # [{'name': 'bob', 'age': 21}, {'name': 'linda', 'age': 19}]

#
# edit data
#
ppl.set(1, {"name":"john","age":45})
print(ppl.get_list()) #[{'name': 'bob', 'age': 21}, {'name': 'john', 'age': 45}, {'name': 'linda', 'age': 19}]
ppl.remove(2)
print(ppl.get_list()) #[{'name': 'bob', 'age': 21}, {'name': 'john', 'age': 45}]

ppl.append({"name":"nana","age":49})
print(ppl.get_list()) #[{'name': 'bob', 'age': 21}, {'name': 'john', 'age': 45}, {'name': 'nana', 'age': 49}]

ppl.insert(1, {"name":"mike","age":30})
print(ppl.get_list()) #[{'name': 'bob', 'age': 21}, {'name': 'mike', 'age': 30}, {'name': 'john', 'age': 45}, {'name': 'nana', 'age': 49}]

```

## Sample usage(load file)


```python
import strl

print(strl.STRL.show_files())  #['test', 'people', 'test2']

#before loading, please change directory to the parent folder of "__stlist__" folder
#mode l load the file. if not exist, create file.
ppl = strl.STRL("people",mode="l")

ppl.delete()

print(strl.STRL.show_files()) #['test', 'test2']

```

