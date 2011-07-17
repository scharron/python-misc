def flatten(ll, rec=False):
  if rec is False:
    assert type(ll) is list and all([type(x) is list for x in ll]), \
           "Cannot flatten a list not containing a list"

  if rec is True and type(ll) is not list:
    return [ll]

  ret = []
  for e in ll:
    if rec is False:
      ret += e
    else:
      ret += flatten(e, True)

  return ret
