##levou algumas horas e um stackoverflow para fazer esse kkkk

def __mdc_(x,y):
    while(y):
        x,y=y,x%y
    return x

def mdc(nums):

    if len(nums) == 2:
        return __mdc_(nums[0], nums[1])
    else:
        mdc_val = __mdc_(nums[0], nums[1])
        nums[0] = mdc_val
        del nums[1]
        return mdc(nums)

mdc([30, 54, 72])
