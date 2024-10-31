from setuptools import setup, find_packages

setup(
    name='serial-generator',  # نام بسته شما
    version='0.1.0',  # نسخه بسته
    author='Your Name',  # نام خود را اینجا قرار دهید
    author_email='your_email@example.com',  # ایمیل خود را اینجا قرار دهید
    description='A simple module to generate random serial numbers.',  # توضیحاتی درباره ماژول
    packages=find_packages(),  # به طور خودکار تمام بسته‌ها را پیدا می‌کند
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # تعیین نوع مجوز
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license='MIT',  # مشخص کردن مجوز
)
