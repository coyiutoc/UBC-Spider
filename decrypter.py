__all__ = ['decrypter']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['printString', 'returnString'])
@Js
def PyJsHoisted_returnString_(aText, jump, this, arguments, var=var):
    var = Scope({'aText':aText, 'jump':jump, 'this':this, 'arguments':arguments}, var)
    var.registers(['jump', 'aText'])
    #for JS loop
    var.put('i', Js(98.0))
    while (var.get('i')<=Js(123.0)):
        try:
            var.put('aText', var.get('aText').callprop('replace', var.get('RegExp').create(var.get('String').callprop('fromCharCode', var.get('i')), Js('g')), var.get('String').callprop('fromCharCode', (var.get('i')-var.get('jump')))))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('aText')
PyJsHoisted_returnString_.func_name = 'returnString'
var.put('returnString', PyJsHoisted_returnString_)
@Js
def PyJsHoisted_printString_(aText, jump, this, arguments, var=var):
    var = Scope({'aText':aText, 'jump':jump, 'this':this, 'arguments':arguments}, var)
    var.registers(['jump', 'aText'])
    var.put('aText', var.get('returnString')(var.get('aText'), var.get('jump')))
    return var.get('aText')
PyJsHoisted_printString_.func_name = 'printString'
var.put('printString', PyJsHoisted_printString_)
pass
pass
pass

def decrypt(first_arg, second_arg):
    return var.get('printString')(Js(first_arg), Js(second_arg))

# Add lib to the module scope
decrypter = var.to_python()

# print(decrypt("Attjtubou Pspgfttps", 1))