# Application Load Balancer

## Usage

```python
from integrator.aws import alb

load_balancer = alb.LoadBalancer(
  'alb',
  ...,
)
target_group = load_balancer.create_target_group(
  'group',
  ...,
)
listener = load_balancer.create_listener(
  'listener',
  target_group=target_group,
  ...,
)
```
