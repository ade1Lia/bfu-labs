import xmlschema

def xmlValidate(xmlPath, xmlSchemaPath):
    try:
        xmlschema.validate(xmlPath, xmlSchemaPath)
        print('ok')
    except Exception as e:
        print(e)

xmlValidate('ex_1.xml','ex_1_schema.xsd')
xmlValidate('ex_1_error.xml','ex_1_schema.xsd')