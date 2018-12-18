# Test execution

## Test #1

```
ansible-playbook -i inventory test.yml -e 'target_group=group1' 
```

This should return a list of `user1`, `user2`, `user3`


## Test #2

```
ansible-playbook -i inventory test.yml -e 'target_group=group2' 
```

This should return a list of `user2`, `user4`, `user5`

