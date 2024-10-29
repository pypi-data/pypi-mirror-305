read -p "Enter project name: " NEW_NAME
OLD_NAME="sphinx-extension"
sed -i "s/$OLD_NAME/$NEW_NAME/g" docs/conf.py
sed -i "s/$OLD_NAME/$NEW_NAME/g" docs/index.rst
sed -i "s/$OLD_NAME/$NEW_NAME/g" README.md
sed -i "s/$OLD_NAME/$NEW_NAME/g" setup.py
sed -i "s/$OLD_NAME/$NEW_NAME/g" $OLD_NAME/__init__.py
mv $OLD_NAME $NEW_NAME
