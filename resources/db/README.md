# Tables

## payment_types

| id | value |
| ------ | ------ |
| 1 | Creadit Card |
| 2 | Cash on Delivery |
| 3 | PayPal |

## user_payment_methods

| id | user_id | payment_type_id | provider | account_number | expiry_date | is_default |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| 1 | 1 | 1 | Master / Visa | number used for payment | yy-mm | True / False |

## product_category

| id | parent_category_id | category_name |
| ------ | ------ | ------ |
| 1 | Null | Clothing |
| 2 | 1 | Slim T-Shirt |
| 3 | Null | Shoes |

## product

| id | category_id | name | description | product_image |
| ------ | ------ | ------ | ------ | ------ |
| 1 | 2 | Slim T-Shirt | Null | Null |
| 2 | 1 | Under Armour joggers | a comfortable pair of jogger pants | Null |
| 3 | 1 | Nike football joggers | a pair of jogger pants with football branding | Null |
| 4 | 1 | Nike tapered joggers | jogger pants have tapered leg | Null |

## variations

what options can be changed on a product
| id | category_id | name |
| ------ | ------ | ------ |
| 1 | 1 | Size |
| 2 | 1 | Color |
| 2 | 1 | Material |

## variation_options

list all of the different possible values for each variations

| id | variation_id | value |
| ------ | ------ | ------ |
| 1 | 1 | XS |
| 2 | 1 | S |
| 3 | 1 | M |
| 4 | 1 | L |
| 5 | 1 | XL |
| 6 | 2 | Gray |
| 7 | 2 | Black |
| 7 | 2 | Dark Blue |

## product_items

this is the instance of the product with all the different options

| id | product_id | sku | qty_in_stock | product_image | price |
| ------ | ------ | ------ | ------ | ------ | ------ |
| 1 | 1 | Slim T-shirt in a color of black and size of M | SKU00000 | Null | 100 |
