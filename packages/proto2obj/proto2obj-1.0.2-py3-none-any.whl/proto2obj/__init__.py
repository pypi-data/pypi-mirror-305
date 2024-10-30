from google.protobuf.descriptor import FieldDescriptor
from google.protobuf.text_format import  Parse , MessageToString
from google.protobuf.json_format import MessageToDict , MessageToJson , ParseDict



class Proto2Obj : 
	PROTOBUF_TYPE_TO_PYTHON_TYPE = {
		FieldDescriptor.TYPE_DOUBLE: 'float',
		FieldDescriptor.TYPE_FLOAT: 'float',
		FieldDescriptor.TYPE_INT64: 'int',
		FieldDescriptor.TYPE_UINT64: 'int',
		FieldDescriptor.TYPE_INT32: 'int',
		FieldDescriptor.TYPE_FIXED64: 'int',
		FieldDescriptor.TYPE_FIXED32: 'int',
		FieldDescriptor.TYPE_BOOL: 'bool',
		FieldDescriptor.TYPE_STRING: 'str',
		FieldDescriptor.TYPE_BYTES: 'bytes',
		FieldDescriptor.TYPE_UINT32: 'int',
		FieldDescriptor.TYPE_ENUM: 'int',
		FieldDescriptor.TYPE_SFIXED32: 'int',
		FieldDescriptor.TYPE_SFIXED64: 'int',
		FieldDescriptor.TYPE_SINT32: 'int',
		FieldDescriptor.TYPE_SINT64: 'int',
	}
	
	def __init__(self, proto) -> None:
		self.proto = proto 


	def fields(self) : 
		return {property_name for property_name, field in self.proto.DESCRIPTOR.fields_by_name.items() }

	def get_fields_type(self) : 
		types_fields = dict()
		for field_name in self.fields() : 
			field = self.proto.DESCRIPTOR.fields_by_name.get(field_name)
			if field.type == field.TYPE_MESSAGE and field.label != field.LABEL_REPEATED  : # memeber type message
				memeber_type  = field.message_type._concrete_class.__name__ 
				if field.message_type._concrete_class.__module__ == self.proto.__module__ : 
					types_fields[field_name] = f'List[{self.proto.__name__}.{memeber_type}]'
				elif field.message_type._concrete_class.__module__ == self.proto.__module__ : 
					types_fields[field_name] = f'List[{memeber_type}]'

			if field.type == field.TYPE_MESSAGE and field.label == field.LABEL_REPEATED  : # memeber type list of message
				memeber_type  = field.message_type._concrete_class.__name__ 
				if field.message_type._concrete_class.__module__ == self.proto.__module__ : 
					types_fields[field_name] = f'List[{self.proto.__name__}.{memeber_type}]'
				elif field.message_type._concrete_class.__module__ == self.proto.__module__ : 
					types_fields[field_name] = f'List[{memeber_type}]'

			if field.type != field.TYPE_MESSAGE and field.label == field.LABEL_REPEATED  : # memeber type list of prirmitive_types
				memeber_type  = self.PROTOBUF_TYPE_TO_PYTHON_TYPE.get(field.type)
				types_fields[field_name] = f'List[{memeber_type}]'		
			
			if field.type != field.TYPE_MESSAGE and field.label != field.LABEL_REPEATED  : # memeber type prirmitive
				memeber_type  = self.PROTOBUF_TYPE_TO_PYTHON_TYPE.get(field.type)
				types_fields[field_name] = f'{memeber_type}'
		return types_fields

	def get_nested_types(self) : 
		nested_types = dict()
		for nested_type_name , nested_type in self.proto.DESCRIPTOR.nested_types_by_name.items() : 
			nested_types[nested_type_name] = Proto2Obj(nested_type._concrete_class).convert()

		return nested_types
	
	def dict_fields(self) : 
		fields = dict()
		for field_name in self.fields() : 
			field = self.proto.DESCRIPTOR.fields_by_name.get(field_name)
			if field.type == field.TYPE_MESSAGE and field.label != field.LABEL_REPEATED  : # memeber type message
				memeber_type  = field.message_type._concrete_class.__name__ 
				fields[field_name] = None

			if field.type == field.TYPE_MESSAGE and field.label == field.LABEL_REPEATED  : # memeber type list of message
				memeber_type  = field.message_type._concrete_class.__name__ 
				fields[field_name] = []

			if field.type != field.TYPE_MESSAGE and field.label == field.LABEL_REPEATED  : # memeber type list of prirmitive_types
				memeber_type  = self.PROTOBUF_TYPE_TO_PYTHON_TYPE.get(field.type)
				fields[field_name] = []			
			
			if field.type != field.TYPE_MESSAGE and field.label != field.LABEL_REPEATED  : # memeber type prirmitive
				memeber_type  = self.PROTOBUF_TYPE_TO_PYTHON_TYPE.get(field.type)
				fields[field_name] = field.default_value
		return fields



	def enums(self) : 
		enums = dict()
		for enum_name , enum_type in self.proto.DESCRIPTOR.enum_types_by_name.items() : 
			enums[enum_name] = {
				key : value 
				for key , value  in enum_type.values_by_name.items()
			}
		return enums

	def enums2obj(self) : 
		result = dict()
		enums = self.enums()
		for enum_name , enum_dict in self.enums().items() : 
			result[enum_name] = type(enum_name , tuple() , enum_dict)
		return result 

	def create__init__method(self) : 
		default_values = self.dict_fields()
		init_code = """def __init__(self, {args}):\n    {body}""".format(
			args=", ".join(f"{key}={repr(value)}" for key, value in default_values.items()),
			body="\n    ".join(f"self._{key} = {key}" for key in default_values)
		)
		local_vars = {}
		exec(init_code, dict(), local_vars)
		return local_vars['__init__']

	def createProperties(self) : 
		result = dict()
		for property_name in self.fields() : 
			scope = dict()
			property_code = f'def property_getter(self, name="{property_name}"): return self._{property_name} \n'
			property_code += f'def property_setter(self, value , name="{property_name}" ): self._{property_name} = value '
			exec(property_code, dict(), scope)
			result[f'{property_name}'] = property(scope['property_getter'] , scope['property_setter'])
		return result

	def convert(self,base = tuple() , attrs = dict()) : 
		base_attrs = dict(__qualname__ = self.proto.__name__)
		base_attrs.update(self.enums2obj())
		base_attrs.update({'__enums__' : sorted(self.enums2obj().keys())})
		base_attrs.update({'__fields__' : sorted(self.get_fields_type())})
		base_attrs.update({'__nested_types__' : sorted(self.get_nested_types())})
		base_attrs.update(self.get_nested_types())
		base_attrs.update({'__init__' : self.create__init__method()}) 
		base_attrs.update({'__protobuf__' : self.proto }) 
		base_attrs.update({'proto' : self.__class__.buildproto }) 
		base_attrs.update(self.createProperties())
		base_attrs.update(attrs)
		return type(self.proto.__name__ , base , base_attrs ) 
	
	def buildproto(self) : 
		instance = self.__protobuf__()
		for field_name in self.__fields__ : 
			attr = getattr(self,field_name,None) # field did not intialized 
			if attr is not None : 
				attr = getattr(self,f'{field_name}')
				field = instance.DESCRIPTOR.fields_by_name.get(field_name)
				if field.type == field.TYPE_MESSAGE and field.label != field.LABEL_REPEATED  : # memeber type message
					getattr(instance , field_name).CopyFrom(attr.to_proto())
				if field.type == field.TYPE_MESSAGE and field.label == field.LABEL_REPEATED  : # memeber type list of message
					[getattr(instance , field_name).append(elem.to_proto()) for elem in attr ] 
				if field.type != field.TYPE_MESSAGE and field.label == field.LABEL_REPEATED  : # memeber type list of prirmitive_types
					[getattr(instance , field_name).append(elem) for elem in attr ]                 
				if field.type != field.TYPE_MESSAGE and field.label != field.LABEL_REPEATED  : # memeber type prirmitive
					setattr(instance , field_name,attr) 
		return instance


__all__ = ['Proto2Obj']
