from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'
        

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class MaterialSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = '__all__'
        

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = '__all__'
    
    
    
class ProductPropSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    material = MaterialSerializer(read_only=True)
    color = ColorSerializer(read_only=True)
    size = ProductSizeSerializer(read_only=True)
    class Meta:
        model = ProductPro
        fields = '__all__'
    
    
class ProductProSerializer(serializers.ModelSerializer):
    material = MaterialSerializer()
    color = ColorSerializer()
    size = ProductSizeSerializer()
    
    class Meta:
        model = ProductPro
        fields = '__all__'
        
 
class ProductAndDetailsSerializer(serializers.ModelSerializer):
    prod = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'
               
    
    def get_prod(self, obj):
        # Get all related ProductPro instances or return an empty list if none exist
        product_pros = obj.prod.all()  # This uses the related_name defined in ProductPro
        return ProductProSerializer(product_pros, many=True).data

class ProductPropUpdateSerializer(serializers.ModelSerializer):
    material = MaterialSerializer()
    color = ColorSerializer()
    size = ProductSizeSerializer()
    class Meta:
        model = ProductPro
        fields = '__all__'


    def update(self, instance, validated_data):
        # Handle nested 'material' update
        material_data = validated_data.pop('material', None)
        if material_data:
            material_id = material_data.get('id', None)
            material_name = material_data.get('name', '').strip()
            if material_id:
                material = Material.objects.get(pk=material_id)
            elif material_name:
                material, _ = Material.objects.get_or_create(name=material_name)
            instance.material = material

        # Handle nested 'color' update
        color_data = validated_data.pop('color', None)
        if color_data:
            color_id = color_data.get('id', None)
            color_name = color_data.get('name', '').strip()
            if color_id:
                color = Color.objects.get(pk=color_id)
            elif color_name:
                color, _ = Color.objects.get_or_create(name=color_name)
            instance.color = color

        # Handle nested 'size' update
        size_data = validated_data.pop('size', None)
        if size_data:
            size_id = size_data.get('id', None)
            size_value = size_data.get('size', '').strip()
            if size_id:
                size = ProductSize.objects.get(pk=size_id)
            elif size_value:
                size, _ = ProductSize.objects.get_or_create(size=size_value)
            instance.size = size

        # Update remaining fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # Save the instance
        instance.save()
        return instance


class ProductPropAddQuantitySerializer(serializers.ModelSerializer):
    material = MaterialSerializer()
    color = ColorSerializer()
    size = ProductSizeSerializer()
    class Meta:
        model = ProductPro
        fields = '__all__'


    def update(self, instance, validated_data):
        # Handle nested 'material' update
        material_data = validated_data.pop('material', None)
        if material_data:
            material_id = material_data.get('id', None)
            material_name = material_data.get('name', '').strip()
            if material_id:
                material = Material.objects.get(pk=material_id)
            elif material_name:
                material, _ = Material.objects.get_or_create(name=material_name)
            instance.material = material

        # Handle nested 'color' update
        color_data = validated_data.pop('color', None)
        if color_data:
            color_id = color_data.get('id', None)
            color_name = color_data.get('name', '').strip()
            if color_id:
                color = Color.objects.get(pk=color_id)
            elif color_name:
                color, _ = Color.objects.get_or_create(name=color_name)
            instance.color = color

        # Handle nested 'size' update
        size_data = validated_data.pop('size', None)
        if size_data:
            size_id = size_data.get('id', None)
            size_value = size_data.get('size', '').strip()
            if size_id:
                size = ProductSize.objects.get(pk=size_id)
            elif size_value:
                size, _ = ProductSize.objects.get_or_create(size=size_value)
            instance.size = size



        # Increment the quantity
        new_quantity = validated_data.get('quantity', None)
        if new_quantity is not None:
            instance.quantity += new_quantity  # Increment the quantity

        # Update remaining fields (if any)
        for attr, value in validated_data.items():
            if attr != 'quantity':  # Skip the quantity as it's already handled
                setattr(instance, attr, value)
       

        # Save the instance
        instance.save()
        return instance

class AllStockSerializer(serializers.ModelSerializer):
    material = MaterialSerializer()
    color = ColorSerializer()
    # size = ProductSizeSerializer()
    class Meta:
        model = StockProperty
        fields = '__all__'


    def update(self, instance, validated_data):
        # Handle nested 'material' update
        material_data = validated_data.pop('material', None)
        if material_data:
            material_id = material_data.get('id', None)
            material_name = material_data.get('name', '').strip()
            if material_id:
                material = Material.objects.get(pk=material_id)
            elif material_name:
                material, _ = Material.objects.get_or_create(name=material_name)
            instance.material = material

        # Handle nested 'color' update
        color_data = validated_data.pop('color', None)
        if color_data:
            color_id = color_data.get('id', None)
            color_name = color_data.get('name', '').strip()
            if color_id:
                color = Color.objects.get(pk=color_id)
            elif color_name:
                color, _ = Color.objects.get_or_create(name=color_name)
            instance.color = color

        # Handle nested 'size' update
        # size_data = validated_data.pop('size', None)
        # if size_data:
        #     size_id = size_data.get('id', None)
        #     size_value = size_data.get('size', '').strip()
        #     if size_id:
        #         size = ProductSize.objects.get(pk=size_id)
        #     elif size_value:
        #         size, _ = ProductSize.objects.get_or_create(size=size_value)
        #     instance.size = size



        # # Increment the quantity
        # new_quantity = validated_data.get('quantity', None)
        # if new_quantity is not None:
        #     instance.quantity += new_quantity  # Increment the quantity

        # Update remaining fields (if any)
        for attr, value in validated_data.items():
            # if attr != 'quantity':  # Skip the quantity as it's already handled
            setattr(instance, attr, value)
       

        # Save the instance
        instance.save()
        return instance


class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
        
class StockPropUpdateSerializer(serializers.ModelSerializer):
    material = MaterialSerializer(read_only=True)
    color = ColorSerializer(read_only=True)
    class Meta:
        model = StockProperty
        fields = '__all__'
        

#    class ProductAndDetailsSerializer(serializers.ModelSerializer):
#     prod = serializers.SerializerMethodField()
#     class Meta:
#         model = Product
#         fields = '__all__'
               
    
#     def get_prod(self, obj):
#         # Get all related ProductPro instances or return an empty list if none exist
#         product_pros = obj.prod.all()  # This uses the related_name defined in ProductPro
#         return ProductProSerializer(product_pros, many=True).data
     

class TaskManagementSerializers(serializers.ModelSerializer):
    # project = ProjectSerializer()
    # assigned_to = EmployeeSerializer()
    class Meta:
        model = Task
        fields = '__all__'       

class AdvancesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Advances
        fields = '__all__'     
        
class EmployeeSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()
    advances = serializers.SerializerMethodField()
    class Meta:
        model = Employees
        fields = '__all__'


    def get_tasks(self, obj):
        tasks = obj.tasks.all()
        return TaskManagementSerializers(tasks, many = True).data
    
    def get_advances(self, obj):
        advances = obj.advances.all()
        return AdvancesSerializers(advances, many = True).data
        
        

        
        

class StockPropertySerializer(serializers.ModelSerializer):
    material = MaterialSerializer(read_only=True)
    color = ColorSerializer(read_only=True)
    
    class Meta:
        model = StockProperty
        fields = '__all__'
        
        

class ExpensesSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    class Meta:
        model = Expenses
        fields = '__all__'
        
        
class AddExpensesSerializer(serializers.ModelSerializer):
    # employee = EmployeeSerializer()
    class Meta:
        model = Expenses
        fields = '__all__'
        
        
    def create(self, validated_data):
        expense = Expenses.objects.create(**validated_data)
        return expense
        
        
        
class AddAdvancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advances
        fields = '__all__'
        
        
    def create(self, validated_data):
        advances = Advances.objects.create(**validated_data)
        return advances
        
        

        
        

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        
        
        
  
        


class WorkInProgressSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    
    class Meta:
        model = WorkInProgress
        fields = '__all__'
        
        


class CartSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    product = ProductPropSerializer()
    
    class Meta:
        model = Cart
        fields = '__all__'
        
class updateTaskSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Task
        fields = '__all__'


class CartCreateSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
   
    class Meta:
        model = Cart
        fields = '__all__'

    def create(self, validated_data):
        customer_data = validated_data.pop('customer')
        print("this is the validated data ", validated_data)
        customer, created = Customer.objects.get_or_create(**customer_data)
        cart = Cart.objects.create(customer=customer, **validated_data)
        return cart
    
    
class CartDepositSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    product = ProductPropSerializer()
    class Meta:
        model = Cart
        fields = '__all__'

    # def create(self, validated_data):
    #     customer_data = validated_data.pop('customer')
    #     print("this is the validated data ", validated_data)
    #     customer, created = Customer.objects.get_or_create(**customer_data)
    #     cart = Cart.objects.create(customer=customer, **validated_data)
    #     return cart
    
    
    
class CreateProductSerializer(serializers.ModelSerializer):
# class AddProductProSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    size = ProductSizeSerializer()
    material = MaterialSerializer()
    
    class Meta:
        model = ProductPro
        fields = '__all__'

    def create(self, validated_data):
        print('Validated data ', validated_data)
        # Get product by ID instead of nested data
        product_id = validated_data.pop('product')
        print('here', product_id)
        product = Product.objects.get(id=product_id.id)  # Get the product by its ID

        # Handle color, size, and material
        product_color = validated_data.pop('color')
        product_size = validated_data.pop('size')
        product_material = validated_data.pop('material')

        color, created = Color.objects.get_or_create(**product_color)
        size, created = ProductSize.objects.get_or_create(**product_size)
        material, created = Material.objects.get_or_create(**product_material)

        # Create the ProductPro instance with the product ID
        productpro = ProductPro.objects.create(
            product=product,  # Assign the product by ID
            color=color,
            size=size,
            material=material,
            **validated_data
        )
        return productpro
    
    
    
    
class CreateStockSerializer(serializers.ModelSerializer):
    material = MaterialSerializer()
    color = ColorSerializer()
    
    class Meta:
        model = StockProperty
        fields = '__all__'
        
        
    
    def create(self, validated_data):
        material_data = validated_data.pop('material')
        material_color = validated_data.pop('color')
        color, created = Color.objects.get_or_create(**material_color)
        material, created = Material.objects.get_or_create(**material_data)
        stockproperty = StockProperty.objects.create(color=color, material=material, **validated_data)
        return stockproperty
    
    
    
class CreateEmployeeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Employees
        fields = '__all__'
        
        
    
    def create(self, validated_data):
        employee = Employees.objects.create(**validated_data)
        return employee
    
    
    
    
    
class CreateProgressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WorkInProgress
        fields = '__all__'
        
    def create(self, validated_data):
        workInprogress = WorkInProgress.objects.create(**validated_data)
        return workInprogress
    
    
    
    
    

class UserRegSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    # email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            # email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
    
    
    
class AddProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        product = Product.objects.create( **validated_data)
        return product
    

class AddProductProSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    size = ProductSizeSerializer()
    material = MaterialSerializer()
    class Meta:
        model = ProductPro
        fields = '__all__'

    def create(self, validated_data):
        # product_data = validated_data.pop('product')
        product_color = validated_data.pop('color')
        product_size = validated_data.pop('size')
        product_material = validated_data.pop('material')
        # product, created = Product.objects.get_or_create(**product_data)
        color, created = Color.objects.get_or_create(**product_color)
        size, created = ProductSize.objects.get_or_create(**product_size)
        material, created = Material.objects.get_or_create(**product_material)
        productpro = ProductPro.objects.create( color=color, size=size, material=material, **validated_data)
        return productpro
    

class SalesAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesAnalytics
        fields = '__all__'



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectName
        fields = '__all__'


class CreateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectName
        fields = '__all__'

    def create(self, validated_data):
        # Create the ProjectName instance

        material = validated_data['material_to_use']
        material_size_required = validated_data['material_size']

        # Check if enough material is available
        if material.total < material_size_required:
            raise ValidationError("Not enough material available in stock.")

        # Reduce the material's size
        material.total -= material_size_required
        material.save()  # Save updated material size in StockProperty


        project = ProjectName.objects.create(**validated_data)
        return project
    

class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        # Create the ProjectName instance
        task = Task.objects.create(**validated_data)
        return task
    
    
class TaskManagementSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    assigned_to = EmployeeSerializer()
    class Meta:
        model = Task
        fields = '__all__'
        


    

class ProjectNameSerializer(serializers.ModelSerializer):
    task_count = serializers.SerializerMethodField()
    class Meta:
        model = ProjectName
        fields = '__all__'

        extra_fields = ['task_count']

    def get_task_count(self, obj):
        return Task.objects.filter(project=obj).count()
    

class AdvancesUpdatesSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Advances
        fields = '__all__'