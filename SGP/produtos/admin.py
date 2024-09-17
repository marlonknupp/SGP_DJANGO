import csv
from django.http import HttpResponse
from django.contrib import admin
from produtos.models import Brand, Category, Product


@admin.register(Brand)
class BrandAmin(admin.ModelAdmin):
    list_display = ('name', 'is_active','description','created_at','updated_at')
    search_fields = ('name',)
    list_filter = ('is_active',)

@admin.register(Category)
class CategoryAmin(admin.ModelAdmin):
    list_display = ('name', 'is_active','description','created_at','updated_at')
    search_fields = ('name',)
    list_filter = ('is_active',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand','category','price',
                    'is_active','created_at','updated_at')
    search_fields = ('title','brand_name','category_name')
    list_filter = ('is_active','brand','category')

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="products.csv"'
        writer = csv.writer(response)
        writer.writerow(['titulo','marca', 'categoria', 'preço',
                          'ativo','descricao','criado em', 'atualizado em'])
        for product in queryset:
            writer.writerow([product.title, product.brand.name, product.category.name,
                              product.price, product.is_active, product.description,
                              product.created_at, product.updated_at])
            return response
        
    export_to_csv.short_description = 'Exportar para CSV'
    actions = [export_to_csv]