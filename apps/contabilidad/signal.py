
def update_credito_debito_asiento(sender,instance,**kwargs):
    if instance.credito > 0:
        instance.asiento.totalCredito = instance.asiento.totalCredito + instance.credito 
        instance.asiento.save()
    
    if instance.debito > 0:
        instance.asiento.totalDebito = instance.asiento.totalDebito + instance.debito 
        instance.asiento.save()
    


def delete_credito_debito_asiento(sender,instance,**kwargs):
    if instance.credito > 0:
        instance.asiento.totalCredito = instance.asiento.totalCredito - instance.credito 
        instance.asiento.save()
    
    if instance.debito > 0:
        instance.asiento.totalDebito = instance.asiento.totalDebito - instance.debito 
        instance.asiento.save()
    

