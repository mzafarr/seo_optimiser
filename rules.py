example_input = '{"mpn": "SKU55900", "Title": "360 degre truck Camara System for Surround View with DvR  ( 4 Cameras ) Â· Semi Truck Vehicle Birds Eye View System Â· 7" Color LCD Monitor ", "product_type": "Vehicles & Parts > Vehicle Parts & Accessories > Motor Vehicle Electronics > 360Â° Backup Camera Systems > Truck", "google_product_category": "Vehicles & Parts > Vehicle Parts & Accessories > Motor Vehicle Electronics > Motor Vehicle Parking Cameras", "description": "This is a our commercial level 360 degree birds eye view camera system designed for semi trucks, trailer and even buses. Upgrade your current vehicle to the most requested safety feature in today vehicle market. This system includes a 7-inch screen and 4 heavy duty wide angle cameras that are easily places around the vehicle with a powerful mobile DVR brain that will stich all 4 cameras together to give you flawless image around your vehicle. The DVR stores all the data in a secured memory card with instant playback features available. The commercial 360 system includes everything you need for for a clean installation, featuring easy to follow instructions and diagrams.", "product_highlight": "\\"4 wide 180 degree angle cameras installed on the FRONT, REAR, LEFT, and RIGHT side of the car for that full 360 Degree image\\",\\"All the cameras have Color and Nightvision\\",\\"Catch sight of the location and obstacles\\",\\"Can record up to 28 hours of your journey\\",\\"Always know your surroundings\\", "brand": "TadiBrothers", "identifier_exists": "yes", "gender": "Unisex", "tax(country:rate:region)": "US:9:CA", "optimized": "No"}'

example_output = '{"mpn": "SKU55900", "Title": "360° Truck Camera System for Surround View with DVR (4 Cameras) · Semi Truck Vehicle Birds Eye View System · 7" Color LCD Monitor", "product_type": "Vehicles & Parts > Vehicle Parts & Accessories > Motor Vehicle Electronics > 360° Backup Camera Systems > Truck", "google_product_category": "Vehicles & Parts > Vehicle Parts & Accessories > Motor Vehicle Electronics > Motor Vehicle Parking Cameras", "description": "This is a our commercial level 360 degree birds eye view camera system designed for semi trucks, trailer and even buses. Upgrade your current vehicle to the most requested safety feature in today vehicle market. This system includes a 7-inch screen and 4 heavy duty wide angle cameras that are easily places around the vehicle with a powerful mobile DVR brain that will stich all 4 cameras together to give you flawless image around your vehicle. The DVR stores all the data in a secured memory card with instant playback features available. The commercial 360 system includes everything you need for for a clean installation, featuring easy to follow instructions and diagrams.", "product_highlight": "4 wide 180 degree angle cameras installed on the FRONT, REAR, LEFT, and RIGHT side of the car for that full 360 Degree image","All the cameras have Color and Nightvision","Catch sight of the location and obstacles","Can record up to 28 hours of your journey","Always know your surroundings", "brand": "TadiBrothers", "identifier_exists": "yes", "gender": "unisex", "tax(country:rate:region)": "US:9:CA", "optimized": "Yes"}'

seo_rules = """
Definitions
Product: This is the actual product that potential customers search for on Google.
Item: This is a product that has been added to your product data, either in a text feed, XML feed, or API. For example, an item is one line in your text feed.
Variant: These are specific versions of a product that comes in different variations. For example, a shirt that comes in different sizes has size variants.
Required: Submit this attribute. If you don't, your product won't be able to serve in ads and free listings.
It depends: You may or may not need to submit this attribute depending on the product or the countries in which your products show.
Optional: You can submit this attribute if you want to help boost your product's performance.

Attribute and format
ID [id]
Your product’s unique identifier
Required
Example
A2B4
Syntax
Max 50 characters
Title [title]
Your product’s name
Required
Example
Mens Pique Polo Shirt
Syntax
Max 150 characters
Description [description]
Your product’s description
Required
Example
Made from 100% organic cotton, this classic red men’s polo has a slim fit and signature logo embroidered on the left chest. Machine wash cold; imported.
Syntax
Max 5000 characters
Link [link]
Your product’s landing page
Required
Example
http://www.example.com/asp/sp.asp?cat=12&id=1030
Image link [image_link]
The URL of your product’s main image
Required
Example
http:// www.example.com/image1.jpg
Additional image link [additional_image_link]
The URL of an additional image for your product
Optional
Example
http://www.example.com/image1.jpg
Syntax
Max 2000 characters
3D model link [virtual_model_link]
Additional link to show a 3D model of your product.
Optional (available only in the US)
Note: This attribute is only available in the classic experience of Merchant Center
Example
https://www.google.com/products/xyz.glb
Mobile link [mobile_link]
Your product’s mobile-optimized landing page when you have a different URL for mobile and desktop traffic
Optional
Example
http://www.m.example.com/asp/ sp.asp?cat=12 id=1030
Syntax
Max 2000 alphanumeric characters

Minimum requirements at a glance
	Use a unique value for each product.
	Use the product's SKU where possible.
	Keep the ID the same when updating your data.
	Use only valid unicode characters.
	Use the same ID for the same product across countries or languages.
	Use a unique value for each product.
	Use the product's SKU where possible.
	Keep the ID the same when updating your data.
	Use only valid unicode characters.
	Use the same ID for the same product across countries or languages.
	Accurately describe your product and match the title from your landing page.
	Don’t include promotional text like "free shipping," all capital letters, or gimmicky foreign characters.
	For variants:
	Include distinguishing features such as color or size.
	For mobile devices:
	Include “with contract” if sold with a contract.
	For the United States, include “with payment plan” if sold in installments.
	For Russia:
	For books and other information products, include the age rating at the beginning of the title.
	Accurately describe your product and match the description from your landing page.
	Don’t include promotional text like "free shipping," all capital letters, or gimmicky foreign characters.
	Include only information about the product. Don’t include links to your store, sales information, details about competitors, other products, or accessories.
	Use formatting (for example, line breaks, lists, or italics) to format your description.
	Use your verified domain name.
	Start with http or https.
	Use an encoded URL that complies with RFC 2396 or RFC 1738.
	Don't link to an interstitial page unless legally required.
	For the image URL:
	Link to the main image of your product.
	Start with http or https.
	Use an encoded URL that complies with RFC 2396 or RFC 1738.
	Make sure the URL can be crawled by Google (robots.txt configuration allowing Googlebot and Googlebot-image).
	For the image:
	Accurately display the product.
	Use an accepted format: JPEG (.jpg/.jpeg), WebP (.webp), PNG (.png), non-animated GIF (.gif), BMP (.bmp), and TIFF (.tif/.tiff).
	Don't scale up an image or submit a thumbnail.
	Don't include promotional text, watermarks, or borders.
	Don't submit a placeholder or a generic image.
	Meet the requirements for the image link [image_link] attribute with these exceptions:
○	The image can include product staging and show the product in use.
○	Graphics or illustrations can be included.
	Submit up to 10 additional product images by including this attribute multiple times.
	Use a 3D model. Your file shouldn’t exceed 15MB. Textures in the file can be up to 2K (4K isn’t supported).
	Provide a valid URL in your product data. The link should point to a .gltf, or .glb file.
	Review your 3D model. You can use a validation tool to verify if your 3D model works properly.
	Meet the requirements for the link [link] attribute.
	
Attribute and format:
Availability [availability]
Your product's availability
Required
Example
in_stock
Supported values
	In stock [in_stock]
	Out of stock [out_of_stock]
	Preorder [preorder]
	Backorder [backorder]
Availability date [availability_date]
Required if product availability is set to preorder
The date a preordered product becomes available for delivery
Example
(For UTC+1)
2016-02-24T11:07+0100
Syntax
	Max 25 alphanumeric characters
	ISO 8601
	YYYY-MM-DDThh:mm [+hhmm]
	YYYY-MM-DDThh:mmZ
Cost of goods sold [cost_of_goods_sold]
Your product’s description
Optional
The costs associated with the sale of a particular product as defined by the accounting convention you set up. These costs may include material, labor, freight, or other overhead expenses. By submitting the COGS for your products, you gain insights about other metrics, such as your gross margin and the amount of revenue generated by your ads and free listings.
Example
23.00 USD
Syntax
	ISO 4217 codes
	Use '.' rather than ',' to indicate a decimal point
	Numeric
Expiration date [expiration_date]
The date that your product should stop showing
Optional
Example
(For UTC+1)
2016-07-11T11:07+0100
Syntax
	Max 25 alphanumeric characters
	ISO 8601
	YYYY-MM-DDThh:mm [+hhmm]
	YYYY-MM-DDThh:mmZ
Price [price]
Your products price
Required
Example
15.00 USD
Syntax
	Numeric
	ISO 4217
Sale price [sale_price]
Your product's sale price
Optional
Example
15.00 USD
Syntax
	Numeric
	ISO 4217
Sale price effective date
[sale_price_effective_date]
The date range during which the sale price applies
Optional
Example
(For UTC+1)
2016-02-24T11:07+0100 /
2016-02-29T23:07+0100
Syntax
	Max 51 alphanumeric characters
	ISO 8601
	YYYY-MM-DDThh:mm [+hhmm]
	YYYY-MM-DDThh:mmZ
	Separate start date and end date with /
Unit pricing measure
[unit_pricing_measure]
The measure and dimension of your product as it is sold
Optional (except when required by local laws or regulations)
Example
1.5kg
Syntax
Numerical value + unit
Supported units
	Weight: oz, lb, mg, g, kg
	Volume US imperial: floz, pt, qt, gal
	Volume metric: ml, cl, l, cbm
	Length: in, ft, yd, cm, m
	Area: sqft, sqm
	Per unit: ct

Google product category [google_product_category]
Optional
Google-defined product category for your product
Example
Apparel & Accessories > Clothing > Outerwear > Coats & Jackets
or
371
Syntax
Value from the Google product taxonomy
	The numerical category ID, or
	The full path of the category
Supported values
Google product taxonomy
Brand [brand]
Your product’s brand name
Required (For all new products, except movies, books, and musical recording brands)
Optional for all other products
Example
Google
Syntax
Max 70 characters

GTIN [gtin]
Your product’s Global Trade Item Number (GTIN)
Required (For all products with a known GTIN to enable full offer performance)
Optional (strongly recommended) for all other products
Example
3234567890126
Syntax
Max 50 numeric characters (max 14 per value - added spaces and dashes are ignored)
Supported values
	UPC (in North America / GTIN-12)
12-digit number like 323456789012
8-digit UPC-E codes should be converted to 12-digit codes
	EAN (in Europe / GTIN-13)
13-digit number like 3001234567892
	JAN (in Japan / GTIN-13)
8 or 13-digit number like 49123456 or 4901234567894
	ISBN (for books)
10 or 13-digit number like 1455582344 or 978-1455582341. If you have both, only include the 13-digit number. ISBN-10 are deprecated and should be converted to ISBN-13
	ITF-14 (for multipacks / GTIN-14)
14-digit number like 10856435001702
MPN [mpn]
Your product’s Manufacturer Part Number (MPN)
Required (Only if your product does not have a manufacturer assigned GTIN)
Optional for all other products
Example
GO12345OOGLE
Syntax
Max 70 alphanumeric characters
Identifier exists [identifier_exists]
Use to indicate whether or not the unique product identifiers (UPIs) GTIN, MPN, and brand are available for your product.
Optional
Example
no
Supported values
	Yes [yes]
Product identifiers are assigned to the new product by the manufacturer
	No [no]
Product lacks a brand, GTIN, or MPN (see requirements to the right). If set to no, still provide the UPIs you have.
	Include only one category.
	Include the most relevant category.
	Include either the full path of the category or the numerical category ID, but not both. It is recommended to use the category ID.
	Include a specific category for certain products.
	Alcoholic beverages must be submitted to only certain categories.
	Mobile devices sold with contract must be submitted as either:
	Electronics > Communications > Telephony > Mobile Phones (ID: 267
	For tablets: Electronics > Computers > Tablet Computers (ID: 4745)
	Gift Cards must be submitted as Arts & Entertainment > Party & Celebration > Gift Giving > Gift Cards & Certificates (ID: 53)
	Include the full category. For example, include Home > Women > Dresses > Maxi Dresses instead of just Dresses
	Only the first product type value will be used to organize bidding and reporting in Google Ads Shopping campaigns
	Provide the brand name of the product generally recognized by consumers.
	Providing the correct brand for a product will ensure the best user experience and result in the best performance.
	Only provide your own brand name as the brand if you manufacture the product or if your product falls into a generic brand category.
	For example, you could submit your own brand name as the brand if you sell private-label products or customized jewelry.
	For products that truly do not have a brand (for example, a vintage dress without a label, generic electronics accessories, etc.) leave this field empty.
	Don't submit values such as "N/A", "Generic", "No brand", or "Does not exist".
	For compatible products:
	Submit the GTIN and brand from the manufacturer who actually built the compatible product.
	Don't provide the Original Equipment Manufacturer (OEM) brand to indicate that your product is compatible with or a replica of the OEM brand's product.
	Exclude dashes and spaces.
	Submit only valid GTINs as defined in the official GS1 validation guide, which includes these requirements:
	The checksum digit is present and correct
	The GTIN is not restricted (GS1 prefix ranges 02, 04, 2)
	The GTIN is not a coupon (GS1 prefix ranges 98 - 99)
	Providing the correct GTIN for a product will ensure the best user experience and result in the best performance.
	Only provide a GTIN if you’re sure it is correct. When in doubt don’t provide this attribute (for example, do not guess or make up a value). If you submit a product with an incorrect GTIN value, your product will be disapproved.
	For compatible products:
	Submit the GTIN and brand from the manufacturer who actually built the compatible product.
	Don't provide the Original Equipment Manufacturer (OEM) brand to indicate that your product is compatible with or a replica of the OEM brand's product.
	For multipacks:
	Use the product identifiers that relates to the multipack.
	For bundles:
	Use the product identifiers for the main product in the bundle.
	If you offer customization, engraving, or other personalization of a product that's been assigned a GTIN by the manufacturer:
	Submit the GTIN and use the bundle [is_bundle] attribute to let Google know that the product includes customization.
	Only submit MPNs assigned by a manufacturer.
	Use the most specific MPN possible.
	For example, different colors of a product should have different MPNs.
	Providing the correct MPN for a product (when required) will ensure the best user experience and result in the best performance.
	Only provide an MPN if you’re sure it’s correct. When in doubt don’t provide this attribute (for example, don’t guess or make up a value).
	If you submit a product with an incorrect MPN value, your product will be disapproved.
	If you don't submit the attribute, the default value is yes.
	Your product’s category type determines which unique product identifiers (GTIN, MPN, brand) are required.
	Submit the identifier exists attribute and set the value to no if:
	Your product is a media item and the GTIN is unavailable (Note: ISBN and SBN codes are accepted as GTINs
	Your product is an apparel (clothing) item and the brand is unavailable
	In all other categories, your product doesn’t have a GTIN, or a combination of MPN and brand
	If a product does have unique product identifiers, don’t submit this attribute with a value of “no” or the product may be disapproved.
	
Attribute and format:
Condition [condition]
The condition of your product at time of sale
Required if your product is used or refurbished
Optional for new products
Example
new
Supported values
	New [new]
Brand new, original, unopened packaging
	Refurbished [refurbished]
Professionally restored to working order, comes with a warranty, may or may not have the original packaging
	Used [used]
Previously used, original packaging opened or missing
Schema.org property: Yes (Learn more)
Adult [adult]
Indicate a product includes sexually suggestive content
Required (If a product contains adult content)
Example
yes
Supported values
	Yes [yes]
	No [no]
Multipack [multipack]
The number of identical products sold within a merchant-defined multipack
Required (For multipack products in Australia, Brazil, Czechia, France, Germany, Italy, Japan, Netherlands, Spain, Switzerland, the UK and the US)
Required for free listings on Google if you’ve created a multipack
Optional for all other products and target countries
Example
6
Syntax
Integer
Bundle [is_bundle]
Indicates a product is a merchant-defined custom group of different products featuring one main product
Required (For bundles in Australia, Brazil, Czechia, France, Germany, Italy, Japan, Netherlands, Spain, Switzerland, the UK and the US)
Required for free listings on Google if you’ve created a bundle containing a main product
Optional for all other products and target countries
Example
yes
Supported values
	Yes [yes]
	No [no]
Certification [certification]
Certifications, such as energy efficiency ratings, associated with your product
Available for the EU and EFTA countries and the UK
Required for products that require certain certification information to be shown in your Shopping ads or free listings, for example due to local energy efficiency labeling regulations
 Optional for all other products
Example
EC:EPREL:123456
Syntax
This attribute uses the following sub-attributes:
	Authority [certification_authority] Certification authority. Only "EC" or "European_Commission" supported.
	Name [certification_name] Name of the certification. Only "EPREL" supported.
	Code [certification_code] Code of the certification. For example, for the EPREL certificate with the link https://eprel.ec.europa.eu/screen/product/dishwashers2019/123456 the code is 123456
Energy efficiency class [energy_efficiency_class]
Your product’s energy label
Available for the EU and EFTA countries and the UK
Optional (except when required by local law or regulations)
Example
A+
Supported values
	A+++
	A++
	A+
	A
	B
	C
	D
	E
	F
	G
Schema.org property: Yes (Learn more)
Minimum energy efficiency class [min_energy_efficiency_class]
Your product’s energy label
Available for the EU and EFTA countries and the UK
Optional (except when required by local laws or regulations)
Available for EU & CH only
Example
A+++
Supported values
	A+++
	A++
	A
	B
	C
	D
	E
	F
	G
Maximum energy efficiency class [max_energy_efficiency]
Your product’s energy label
Available for the EU and EFTA countries and the UK
Optional (except when required by local laws or regulations)
Available for EU & CH only
Example
D
Supported values
	A+++
	A++
	A
	B
	C
	D
	E
	F
	G
Age group [age_group]
The demographic for which your product is intended
Required (For all apparel products that are targeted to people in Brazil, France, Germany, Japan, the UK, and the US as well as all products with assigned age groups)
Required for free listings for all Apparel & Accessories (ID: 166) products
Optional for all other products and target countries
Example
infant
Supported values
	Newborn [newborn]
0-3 months old
	Infant [infant]
3-12 months old
	Toddler [toddler]
1-5 years old
	Kids [kids]
5-13 years old
	Adult [adult]
Teens or older
Color [color]
Your product’s color(s)
Required (For all apparel products that are targeted to Brazil, France, Germany, Japan, the UK, and the US as well as all products available in different colors)
Required for free listings for all Apparel & Accessories (ID: 166) products
Optional for all other products and target countries
Example
Black
Syntax
Max 100 alphanumeric characters (max 40 characters per color)
Gender [gender]
The gender for which your product is intended
Required (Required for all apparel items that are targeted to people in Brazil, France, Germany, Japan, the UK, and the US as well as all gender-specific products)
Required for free listings for all Google Apparel & Accessories (ID: 166) products
Optional for all other products and target countries
Example
Unisex
Supported values
	Male [male]
	Female [female]
	Unisex [unisex]
Material [material]
Your product’s fabric or material
Required (if relevant for distinguishing different products in a set of variants)
Optional for all other products
Example
leather
Syntax
Max 200 characters

Pattern [pattern]
Your product’s pattern or graphic print
Required (if relevant for distinguishing different products in a set of variants)
Optional for all other products
Example
striped
polka dot
paisley
Syntax
Max 100 characters
Size [size]
Your product’s size
Required (Required for all apparel products in Apparel & Accessories > Clothing (ID:1604) and Apparel & Accessories > Shoes (ID:187) categories targeted to people in Brazil, France, Germany, Japan, the UK, and the US as well as all products available in different sizes)
Required for free listings for all Apparel & Accessories > Clothing (ID:1604) and Apparel & Accessories > Shoes (ID:187) products
Optional for all other products and target countries
Example
XL
Syntax
Max 100 characters
Size type [size_type]
Your apparel product’s cut
Optional (Available for apparel products only)
Example
maternity
Supported values
	Regular [regular]
	Petite [petite]
	Maternity [maternity]
	Big [big]
	Tall [tall]
	Plus [plus]
Size system [size_system]
The country of the size system used by your product
Optional (Available for apparel products only)
Example
US
Supported values
	US
	UK
	EU
	DE
	FR
	JP
	CN
	IT
	BR
	MEX
	AU
Item group ID [item_group_id]
ID for a group of products that come in different versions (variants)
Required (Brazil, France, Germany, Japan, the United Kingdom, and the US if the product is a variant)
Required for free listings for all product variants
Optional for all other products and target countries
Example
AB12345
Syntax
Max 50 alphanumeric characters
Product length [product_length]
Your product's length
Optional
Example
20 in
Syntax
Number + unit
Supported values
1-3000
	Decimal values are supported
Supported units
	cm
	in
Product width [product_width]
Your product's width
Optional
Example
20 in
Syntax
Number + unit
Supported values
1-3000
	Decimal values are supported
Supported units
	cm
	in
Product height [product_height]
Your product's height
Optional
Example
20 in
Syntax
Number + unit
Supported values
1-3000
	Decimal values are supported
Supported units
	cm
	in
Product weight [product_weight]
Your product's weight
Optional
Example
3.5 lb
Syntax
Number + unit
Supported values
0-2000
	Decimal values are supported
Supported units
	lb
	oz
	g
	kg
	Product detail [product_detail]
	Technical specifications or additional details of your product
	Optional
	Example
General:Product Type:Digital player
	Syntax
This attribute uses 3 sub-attributes:
	Section name [section_name]: Max 140 characters
	Attribute name [attribute_name]: Max 140 characters
	Attribute value [attribute_value]: Max 1000 characters
	Schema.org property: No
	Product highlight [product_highlight]
	The most relevant highlights of your products
	Optional
	Example
Supports thousands of apps, including Netflix, YouTube, and HBO Max
	Syntax
Max 150 characters
	Schema.org property: No
Minimum requirements at a glance
	Set the value of this attribute to yes if this individual product contains nudity or sexually suggestive content. If you don't submit the attribute, the default value is no. Learn about the adult-oriented content policy
	If your website is generally focused on an adult audience and contains adult-oriented content with or without nudity, indicate that in your Merchant Center settings.
	If you use Merchant Center Next, find these settings in the Business details tab.
	If you use the classic Merchant Center, find these settings under “Tools & Settings” and then select “Account”.
	Submit this attribute if you defined a custom group of identical products and are selling them as a single unit of sale (for example, you're selling 6 bars of soap together).
	Submit the number of products in your multipack. If you don't submit the attribute, the default value is 0.
	If the product's manufacturer assembled the multipack instead of you, don't submit this attribute.
	Submit yes if you're selling a custom bundle of different products that you created, and the bundle includes a main product (for example, a camera combined with a lens and bag). If you don't submit the attribute, the default value is no.
	Don't use this attribute for bundles without a clear main product (for example, a gift basket containing cheese and crackers).
Consult EU energy efficiency regulations or any applicable local law to determine if you need to provide this attribute.  This includes products covered by rescaled EU energy labels, for example:
	Fridges and freezers
	Dishwashers 
	Televisions and other external monitors
	Household washing machines and washer-dryers
	Refrigerating appliances with a direct-sales function
	Light sources
For products that have not been rescaled or cannot be located in the EU EPREL database, you can use the energy efficiency class [energy_efficiency_class], minimum energy efficiency class [min_energy_efficiency_class], and maximum energy efficiency class [max_energy_efficiency_class] attributes.
	Include the legally required energy label.
	To be used in combination with minimum energy efficiency class [min_energy_efficiency_class] and maximum energy efficiency class [max_energy_efficiency_class] to create an energy efficiency label, for example, A+ (A+++ to G).
	Include the legally required energy label.
	To be used in combination with energy efficiency class [energy_efficiency_class] and maximum energy efficiency class [max_energy_efficiency_class] to create an energy efficiency label, for example, A+ (A+++ to D).
	Include the legally required energy label
	To be used in combination with energy efficiency class [energy_efficiency_class] and minimum energy efficiency class [min_energy_efficiency_class] to create a textual or graphical energy efficiency label, for example, A+ (G to A+++)
	Include one value per product.
	For variants:
	Include the same value for item group ID [item_group_id] and different values for age group.
	Don’t use a number such as "0", "2", or "4".
	Don’t use characters that aren’t alphanumeric such as "#fff000".
	Don’t use only one letter such as R. (For Chinese, Japanese, or Korean languages, you can include a single character such as 红.)
	Don’t reference the product or image such as “see image”.
	Don't combine several color names into one word, such as "RedPinkBlue". Instead, separate them with a /, such as "Red/Pink/Blue". Don’t use a value that isn’t a color, such as "multicolor", "various", "variety", "men's", "women's", or "N/A".
	If your product features multiple colors, list the primary color first.
	For variants:
	Include the same value for item group ID [item_group_id] and different values for color [color]
	For some Apparel & Accessories (ID:166) categories like Shoelaces (ID:1856), this attribute is recommended instead of required since these categories aren't dependent on gender.
	For variants:
	Include the same value for item group ID [item_group_id] and different values for gender
	To indicate multiple materials for a single product (not variants), add a primary material, followed by up to 2 secondary materials, separated by a /.
	For example, instead of "CottonPolyesterElastane", use "cotton/polyester/elastane".
	For variants:
	Include the same value for the item group ID [item_group_id] attribute and different values for the material attribute
	For variants:
	Include the same value for the item group ID [item_group_id] attribute and different values for the pattern attribute
	For variants:
	Include this with the same value for item group ID [item_group_id] and different values for size [size]
	If sizes contain multiple dimensions, condense them into one value. For example, "16/34 Tall" is for neck size of 16 inches, sleeve length of 34 inches, and “Tall” fit
	If your item is one size fits all or one size fits most, you can use one_size, OS, one_size fits_all, OSFA, one_size_fits_most, or OSFM.
	For merchant-defined multipack products, submit the multipack quantity using the multipack [multipack] attribute. Do not submit the multipack quantity under the size attribute.
	Submit up to 2 values.
	If you don't submit the attribute, the default value is regular.
	If you don't submit the attribute, the default value is your target country.
	Use a unique value for each group of variants. Use the parent SKU where possible.
	Keep the value the same when updating your product data.
	Use only valid unicode characters.
	Use an item group ID for a set of products that differ by one or more of these attributes:
	Color [color]
	Size [size]
	Pattern [pattern]
	Material [material]
	Age group [age_group]
	Gender [gender]
	Include the same attributes for each product in the item group. For example, if a product varies by size and color, submit size [size] and color [color] for every product that share the same value for item group ID [item_group_id].
	If your products differ by design elements that aren't represented by the attributes above, don't use item group ID.
	Include as many of the product measurement attributes as possible.
	Use the same unit of measurement for each product dimension attribute (including product length, width, and height). Otherwise, the information won't be displayed.
	Include as many of the product measurement attributes as possible.
	Use the same unit of measurement for each product dimension attribute (including product lengths, width, and height). Otherwise, the information won't be displayed.
	Include as many of the product measurement attributes as possible.
	Use the same unit of measurement for each product dimension attribute (including product lengths, width, and height). Otherwise, the information won't be displayed.
	Use the actual assembled product weight for this attribute.
	If your product comes in multiple pieces, for example, as part of a bundle, use the complete weight of all the pieces in the listing.
	Don't add information covered in other attributes, all capital letters, gimmicky foreign characters, promotion text, or list keywords or search terms.
	Don’t add information such as price, sale price, sale dates, shipping, delivery date, other time-related information, or your company’s name.
	Only provide an attribute name and value when the value is confirmed. For example, provide “Vegetarian=False” if a food product is not vegetarian.
	Use between 2 and 100 product highlights.
	Describe only the product itself.
	Don't list keywords or search terms.
	Don’t include promotional text, all capital letters, or gimmicky foreign characters.
	
	Attribute and format:
Ads redirect [ads_redirect]
	A URL used to specify additional parameters for your product page. Customers will be sent to this URL rather than the value that you submit for the link [link] or mobile link [mobile_link] attributes
	Optional
	Example
http://www.example.com/product.html
	Syntax
Max 2000 characters
	Custom label 0-4 [custom_label_0-4]
	Label that you assign to a product to help organize bidding and reporting in Shopping campaigns
	Optional
	Example
Seasonal 
Clearance
Holiday
Sale
Price range
	Syntax
Max 100 characters
	Schema.org property: No
	Promotion ID [promotion_id]
	An identifier that allows you to match products to promotions
	Optional (Required for promotions in Australia, France, Germany, India, the UK and the US)
	Example
ABC123
	Syntax
Max 50 characters
	Schema.org property: No
	Lifestyle image link [lifestyle_image_link]
	Optional
	Attribute used to include the URL for a lifestyle image for your product
	Only available for browsy surfaces, such as Discovery ads
	Example
	https://www.example.com/image1.jpg
	Syntax
	Max 2000 characters
	External seller ID [external_seller_id]
	Note: Marketplaces is currently only available in the classic version of Merchant Center.Required for multi-seller account
	Used by a marketplace to externally identify a seller. (For example, on a website)
	Example
	SellerPublicName1991
	Syntax
	1 - 50 characters
	Excluded destination [excluded_destination]
	A setting that you can use to exclude a product from participating in a specific type of advertising campaign
	Optional
	Example
Shopping_ads
	Supported values
	Shopping_ads
	Buy_on_Google_listings
	Display_ads
	Local_inventory_ads
	Free_listings
	Free_local_listings
	YouTube_Shopping
	Some values only available for the classic version of Merchant Center.
	Schema.org property: No
	Included destination [included_destination]
	A setting that you can use to include a product in a specific type of advertising campaign
	Optional
	Example
Shopping_ads
	Supported values
	Shopping_ads
	Buy_on_Google_listings
	Display_ads
	Local_inventory_ads
	Free_listings
	Free_local_listings
	YouTube_Shopping
	Some values only available for the classic version of Merchant Center.
	Schema.org property: No
	Excluded countries for Shopping ads [shopping_ads_excluded_country]
	A setting that allows you to exclude countries where your products are advertised on Shopping ads
	Optional
	Only available for Shopping ads
	Example
DE
	Syntax
2 characters. Must be an ISO_3166-1_alpha-2 country code.
	Schema.org property: No
	Pause [pause]
	A setting you can use to pause and quickly reactivate a product for all ads (including Shopping ads, Display ads, and local inventory ads). A product can be paused for up to 14 days. If a product is paused for more than 14 days it will be disapproved. To re-approve, remove the attribute.
	Optional
	Example
ads
	Supported values
ads
	Schema.org property: No
	Shipping [shipping]
	Your product's shipping cost, shipping speeds, and the locations your product ships to
	It depends
	Shipping costs are required for Shopping ads and free listings for the following countries: Australia, Austria, Belgium, Canada, Czechia, France, Germany, Ireland, Israel, Italy, Japan, the Netherlands, Poland, South Korea, Spain, Switzerland, the UK, and the US
	You may also be required to provide shipping costs based on local laws or regulations.
	Optional (to specify additional countries your product ships to or destinations where shipping costs are not required)
	Supported prices
0–1000 USD (check for other currencies)
	Example
US:CA:Overnight:16.00 USD:1:1:2:3
	Syntax
This attribute uses the following sub-attributes:
	Country [country] (Required)
ISO 3166 country code
	Region [region](Optional)
	Postal code [postal_code](Optional)
	Location ID [location_id] (Optional)
	Location group name [location_group_name] (Optional)
	Service [service] (Optional)
Service class or shipping speed
	Price [price] (Optional)
Fixed shipping cost, including VAT if required
	Minimum handling time [min_handling_time] and maximum handling time [max_handling_time] (Optional)
To specify handling time
	Minimum transit time [min_transit_time] and maximum transit time [max_transit_time] (Optional)
To specify transit time
	Schema.org property: Yes (Learn more)
	Shipping label [shipping_label]
	Optional
	Label that you assign to a product to help assign correct shipping costs in Merchant Center account settings
	Example
	perishable
	Syntax
	Max 100 characters
	Schema.org property: No
	Shipping weight [shipping_weight]
	The weight of the product used to calculate the shipping cost
	Optional (Required for carrier-calculated rates in your account shipping settings)
	Supported weights
	0–2000 lbs for imperial
	0–1000 kgs for metric
	Example
3 kg
	Syntax
Number + unit
	Supported units
	lb
	oz
	g
	kg
	Schema.org property: No
Shipping length [shipping_length]
The length of the product used to calculate the shipping cost by dimensional weight
Optional (Required for carrier-calculated rates in your account shipping settings)
Example
20 in
Syntax
Number + unit
Supported values
	1 - 150 for inches
	1 - 400 for cm
Supported units
	in
	cm
Shipping width [shipping_width]
The width of the product used to calculate the shipping cost by dimensional weight
Optional (Required for carrier-calculated rates in your account shipping settings)
Example
20 in
Syntax
Number + unit
Supported values
	1 - 150 for inches
	1 - 400 for cm
Supported units
	in
	cm
Schema.org property: No

Shipping height [shipping_height]
The height of the product used to calculate the shipping cost by dimensional weight
Optional (Required for carrier-calculated rates in your account shipping settings)
Example
20 in
Syntax
Number + unit
Supported values
	1 - 150 for inches
	1 - 400 for cm
Supported units
	in
	cm
Schema.org property: No
Ships from country [ships_from_country]
A setting that allows you to provide the country from which your product will typically ship
Optional
Example
DE
Syntax
2 characters. Must be an ISO_3166-1_alpha-2 country code.
Maximum handling time [max_handling_time]
The longest amount of time between when an order is placed for a product and when the product ships
Optional
Example
3
Syntax
Integer, greater than or equal to 0
Schema.org property: No
Transit time label [transit_time_label]
Optional
Label that you assign to a product to help assign different transit times in Merchant Center account settings.
Example
From Seattle
Syntax
Max 100 characters
Minimum handling time [min_handling_time]
The shortest amount of time between when an order is placed for a product and when the product ships
Optional
Example
1
Syntax
Integer, greater than or equal to 0
Schema.org property: No
Tax [tax]
Your product’s sales tax rate in percent
Required (Available for the US only)
Example
US:CA:5.00:y
Syntax
This attribute uses 4 sub-attributes:
	Rate [rate] (required)
Tax rate as a percentage
	Country [country] (optional)
ISO 3166 country code
	Region [region] or postal code [postal_code] or location ID [location_id] (optional)
	Shipping tax [tax_ship] (optional)
Specify if you charge tax on shipping.
	Supported values:
	yes or no
Schema.org property: No

Tax category [tax_category]
A category that classifies your product by specific tax rules
Optional (Recommended for custom tax rates at the account level)
Example
Apparel
Syntax
Max 100 characters
Schema.org property: No
	Minimum requirements at a glance:
	Submit the same registered domain as for the link [link]attribute (and the mobile link [mobile_link]attribute, if present).
	Valid registered domains include "example.com", "m-example.com", "example.co.uk", "example.com.ai", and "bar.tokyo.jp".
	URLs submitted with invalid domains, such as "example.zz" or "example.comic", will not be accepted. For more details on valid registered domains, see ads redirect.
	Use a value that you'll recognize in your Shopping campaign. The value won't be shown to customers who see your ads and free listings.
	Submit up to 5 custom labels per product by including this attribute multiple times:
	custom_label_0
	custom_label_1
	custom_label_2
	custom_label_3
	custom_label_4
	Use only 1,000 unique values for each custom label across your Merchant Center account.
	Use a unique and case sensitive ID without spaces or symbols (for example, %, !).
	To map specific promotions to specific products, submit the same promotion ID in your product data and promotion data.
	Submit up to 10 promotion IDs for one product by including this attribute multiple times.
	Use a URL that points to an image in a supported file format
	Start with http or https and comply with RFC 3986
	Replace any symbols or spaces with URL encoded entities
	Make sure Google can crawl your URL
	Use a unique value for each seller.
	Keep the ID the same when updating your data
	Use only valid characters. Avoid invalid characters like control, function, or private area characters
	Use the same ID for the same seller across countries or languages
	Use this setting when shipping costs for your product are not defined in your Merchant Center account or when you need to override shipping costs or speeds defined in your Merchant Center account.
	Use a value that you'll recognize in your account shipping settings. The value won't be shown to customers. Examples:
	Sameday
	Oversize
	Only FedEx
	
	Submit this value if you set up account shipping settings for carrier-calculated rates or weight-based shipping services
	
	Submit this value if you set up account shipping settings for carrier-calculated rates.
	If you don't provide shipping dimension attributes while using carrier-calculated rates, Google won't be able to calculate rates based on the dimensional weight of the product. If that's the case, we'll just calculate the rates based on the value you provided in the shipping weight [shipping_weight] attribute.
	If you submit this attribute, submit all shipping dimension attributes:
	Shipping length [shipping_length]
	Shipping width [shipping_width]
	Shipping height [shipping_height]
	Use the same unit for all shipping dimension attributes that apply to a single product.
	Google doesn't automatically calculate additional shipping cost for oversized products. If your package would be considered large or oversized by your carrier, you should use the shipping [shipping] attribute to set shipping cost for an individual product.
	Meet the requirements for the shipping length [shipping_length] attribute.
	Meet the requirements for the shipping length [shipping_length] attribute.
	Provide only the country from which you typically ship this product.
	Submit this attribute if you want to display the overall time it takes for a product to arrive at its destination.
	Submit the number of business days (as configured in Merchant Center).
	For products ready to be shipped the same day, submit 0.
	For submitting a time range submit maximum handling time [max_handling_time] in combination with minimum handling time [min_handling_time].
	Meet the requirements for the maximum handling time [max_handling_time] attribute.
	Use this setting only to override the account tax settings for an individual product. We recommend that you submit tax information for all your products using the account settings in Merchant Center.
	For the US and Canada:
	Don't include tax in the price [price] attribute.
	For the US only, include the tax in the tax [tax] attribute if you need to override your account settings.
	For all other countries:
	Include value added tax (VAT) or Goods and Services Tax (GST) in the price attribute and do not use the tax attribute.
	Use this attribute if you have products that have a specific tax rate.
	Category labels in your product data must match the labels you enter in the Categories section in Merchant Center.
"""