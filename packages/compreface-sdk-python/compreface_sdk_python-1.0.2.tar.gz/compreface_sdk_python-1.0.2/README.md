# compreface-sdk-python

https://github.com/exadel-inc/CompreFace  Python SDK

Rest-API-description https://github.com/exadel-inc/CompreFace/blob/master/docs/Rest-API-description.md

# Installation

It can be installed through pip:

```shell
pip install compreface-sdk-python
```

## Initialization
First, you need the Compreface application. For more details, please refer to https://github.com/exadel-inc/CompreFace.



```python
from compare.core.compare_face import CompareFace

DOMAIN: str = 'http://localhost'
PORT: int = 8000
API_KEY: str = 'your_face_recognition_key'

compare = CompareFace("DOMAIN", PORT)
rec_service = compare.init_recognition_service('your_face_recognition_service_key')
detect_service = compare.init_detect_service('your_detection_service_key')
verify_service = compare.init_verify_service('your_verification_service_key')
# get all subjects
rv = rec_service.get_all_subjects()

```
