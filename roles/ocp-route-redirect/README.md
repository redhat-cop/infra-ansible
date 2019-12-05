# Overview
This role allows you to retrieve the url of a redirected route

## Why?
A majority of the time, this isn't a problem. But whenever you're using the value of a route to do certain REST actions and they don't get redirected appropriately, this can be problematic. An example of this is when you're doing a POST against what you believe to be the route value (i.e. the http endpoint), but then it gets redirected to the true endpoint (i.e. https endpoint). What happens behind the scenes can frequently be that your client (ex. Ansible) hits the first endpoint, gets redirected and does a GET for the second redirected endpoint. This unintentionally drops the body of your request, resulting in the POST action never happening.

## Usage:
```yaml
tasks:
- include_role:
    name: ocp-redirect-route
  vars:
    redirect_route_name: my-route-name
    redirect_route_namespace: my-route-namespace
    redirect_route_var_name: name-of-var-i-want-to-store-route-value
```

## Example
```yaml
- include_role:
    name: ocp-redirect-route
  vars:
    redirect_route_name: ansible-tower-web-svc
    redirect_route_namespace: ansible-tower
    redirect_route_var_name: default_tower_url
```
