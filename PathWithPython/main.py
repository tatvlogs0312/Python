from pathlib import Path

# Kiểm tra đường dẫn tồn tại ko?
pathEcommerce = Path("ecommerce")
print(pathEcommerce.exists())

# tạo một thư mục mới
pathEmail = Path("emails")
if not pathEmail.exists():
    pathEmail.mkdir()

path = Path()
print(path.glob('*.py'))

for file in path.glob('*.py'):
    print(file)

for file in path.glob('*'):
    print(file)
