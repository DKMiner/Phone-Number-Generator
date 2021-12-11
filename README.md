# CVE-2019-15514
**Type:** Information Disclosure

**Affected Users, Versions, Devices:** All Telegram Users

## Description
Suppose `ali` is hacktivist. His telegram user ID is `21788973` and mobile number is hidden. He lives in pakistan (+92).
We can add any user to contact by phone number. We will add phones numbers from range `+92-0000000000` to `+92-9999999999`.
So if any number successfully added and that user ID is `21788973`, that's mean `ali` number is successfully exposed !

**Note:** All above information supplied is hypothetical.

Remember, current example range was 9 digits long. We can reduce it more by social engineerring, sim code knowledge, password resets (specially gmail,paypal)...
The more low range, the more less time will it take.

## Background
This bug been exploited in wild from long. This appreciated us to investigate and open source its exploit for making telegram to patch it soon. 

## Proof Of Concept
**Generate number range:**

Suppose, we have an telegram victim that number starts with `92313`, ends with `89` and in between there are `5` unknown digits 
We will generate all comibnations of number list within range `92313-xxxxx-89`. Use [num_gen.py](num_gen.py)
- [prefix](num_gen.py#L1): a number should starts with. Here example, its `92313`
- [middle_range](num_gen.py#L2): total digits of unknown middle range. Here example, its `5`
- [suffix](num_gen.py#L3): a number should ends with. Here example, its `89`

