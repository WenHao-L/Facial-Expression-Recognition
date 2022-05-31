import torch



# output : batch_size * 7 ,target_size : batch_size * 1
def accuracy(output, target):

    with torch.no_grad():
        batch_size = target.size(0)
        pred = torch.argmax(output, dim=1)  #取output最大的
        correct = pred.eq(target).float().sum(0)
        acc = correct * 100 / batch_size
    return [acc]


'''
def accuracy(output, target, topk=(1,)):
    """Computes the accuracy over the k top predictions for the specified values of k"""
    with torch.no_grad():
        maxk = max(topk)
        batch_size = target.size(0)

        _, pred = output.topk(maxk, 1, True, True)
        pred = pred.t()
        correct = pred.eq(target.view(1, -1).expand_as(pred))

        res = []
        for k in topk:
            correct_k = correct[:k].view(-1).float().sum(0, keepdim=True)
            res.append(correct_k.mul_(100.0 / batch_size))
        return res
'''
