# Recipes are laid out for ease of reading and updating.

def dictionary_builder(name, jpn, image, buff, category, description):
    row = {"name": name, "image": image, "buff": buff, "category": category, "jpn": jpn, "description": description}
    return row


def apple_pie():
    name = "apple pie"
    jpn = "アップルパイ"
    image = "Apple-Pie.png"
    buff = "NONE"
    category = "FRUITS DESSERT"
    description = "The crispy, flaky pie crust and sweet apples are a match made in heaven."
    return dictionary_builder(name, jpn, image, buff, category, description)


def carrot_cake():
    name = "carrot cake"
    jpn = "ニンジンケーキ"
    image = "Carrot-Cake.png"
    buff = "ENDURING HASTY"
    category = "VEGETABLES DESSERT"
    description = "Even those who don't like carrots tend to enjoy the mild sweetness of this cake."
    return dictionary_builder(name, jpn, image, buff, category, description)


def ceremonial_platter():
    name = "ceremonial platter"
    jpn = "セレモニアルプレート"
    image = "Ceremonial-Platter.png"
    buff = "ENDURING"
    category = "MEAT"
    description = "A dish served at the Champions' inauguration ceremony with ingredients everyone can enjoy."
    return dictionary_builder(name, jpn, image, buff, category, description)


def clam_chowder():
    name = "clam chowder"
    jpn = "貝のチャウダー"
    image = "Clam-Chowder.png"
    buff = "HEARTY"
    category = "SEAFOOD SOUP"
    description = "The nutritional value of hearty blueshell snail combines with butter and milk in a rich soup."
    return dictionary_builder(name, jpn, image, buff, category, description)


def deya_hot_pot():
    name = "deya hot pot"
    jpn = "アデヤ鍋"
    image = "Deya-Hot-Pot.png"
    buff = "TOUGH MIGHTY"
    category = "SOUP OTHER"
    description = "A hot-pot dish made from thoroughly stewed local fish. A favorite of visitors to Deya Village."
    return dictionary_builder(name, jpn, image, buff, category, description)


def egg_pudding():
    name = "egg pudding"
    jpn = "たまごプリン"
    image = "Egg-Pudding.png"
    buff = "NONE"
    category = "DESSERT"
    description = "Made by cooking eggs and milk in a special mold, its soft texture melts in your mouth."
    return dictionary_builder(name, jpn, image, buff, category, description)


def egg_tart():
    name = "egg tart"
    jpn = "エッグタルト"
    image = "Egg-Tart.png"
    buff = "NONE"
    category = "DESSERT"
    description = "You'll know this simple dessert is done baking when it smells just delightful."
    return dictionary_builder(name, jpn, image, buff, category, description)


def fish_pie():
    name = "fish pie"
    jpn = "フィッシュパイ"
    image = "Fish-Pie.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "SEAFOOD"
    description = "A mainstay in any fisherman's home, the crisp crust pairs well with the fishy flavor."
    return dictionary_builder(name, jpn, image, buff, category, description)


def carrot_stew():
    name = "carrot stew"
    jpn = "ニンジンシチュー"
    image = "Carrot-Stew.png"
    buff = "ENDURING ENERGIZING HASTY"
    category = "OTHER"
    description = "This simple stew sat simmering for a long time to bring out the sweetness of the carrots."
    return dictionary_builder(name, jpn, image, buff, category, description)


def crab_omelet_with_rice():
    name = "crab omelet with rice"
    jpn = "カニ玉チャーハン"
    image = "Crab-Omelet-With-Rice.png"
    buff = "MIGHTY TOUGH ENERGIZING"
    category = "SEAFOOD"
    description = "The fluffy crab legs pair perfectly with the rice for a truly scrumptious dish."
    return dictionary_builder(name, jpn, image, buff, category, description)


def crab_risotto():
    name = "crab risotto"
    jpn = "カニリゾット"
    image = "Crab-Risotto.png"
    buff = "MIGHTY TOUGH ENERGIZING"
    category = "SEAFOOD"
    description = "An everyday stable of seaside villages, the secret to its delicious flavor lies in crab fat."
    return dictionary_builder(name, jpn, image, buff, category, description)


def crab_stir_fry():
    name = "crab stir-fry"
    jpn = "炒めガニ"
    image = "Crab-Stir-Fry.png"
    buff = "MIGHTY TOUGH ENERGIZING"
    category = "SEAFOOD"
    description = "The Goron spice used in preparing this crab pairs perfectly with the flavor of the meat."
    return dictionary_builder(name, jpn, image, buff, category, description)


def cream_of_mushroom():
    name = "cream of mushroom"
    jpn = "キノコのクリーム"
    image = "Cream-of-Mushroom-Soup.png"
    buff = "ENDURING HASTY TOUGH"
    category = "SOUP"
    description = "The creamy mushroom and vegetable soup is so chunky it eats like a meal!"
    return dictionary_builder(name, jpn, image, buff, category, description)


def cream_of_vegetable_soup():
    name = "cream of vegetable soup"
    jpn = "野菜のクリーム"
    image = "Cream-of-Vegetable-Soup.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "SOUP VEGETABLES"
    description = "Made by simmering vegetables in milk, this healthy dish is as simple as the ingredients."
    return dictionary_builder(name, jpn, image, buff, category, description)


def creamy_heart_soup():
    name = "creamy heart soup"
    jpn = "ハートミルクスープ"
    image = "Creamy-Heart-Soup.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "SOUP"
    description = "Enjoying this sweet soup with another person will bring you closer together."
    return dictionary_builder(name, jpn, image, buff, category, description)


def creamy_meat_soup():
    name = "creamy meat soup"
    jpn = "クリーミーな肉のスープ"
    image = "Creamy-Meat-Soup.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "SOUP"
    description = "This nutritious soup contains serious portions of lightly-braised meat and many vegetables."
    return dictionary_builder(name, jpn, image, buff, category, description)


def creamy_seafood_soup():
    name = "creamy seafood soup"
    jpn = "ハートミルクスープ"
    image = "Creamy-Seafood-Soup.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "SOUP"
    description = "Thick-cut chunks of seafood and stock provides a satisfying savoriness."
    return dictionary_builder(name, jpn, image, buff, category, description)


def curry_pilaf():
    name = "curry pilaf"
    jpn = "カレーピラフ"
    image = "Curry-Pilaf.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "RICE VEGETABLES"
    description = "The Goron spice used in this pilaf has given it a rich, spicy aroma."
    return dictionary_builder(name, jpn, image, buff, category, description)


def curry_rice():
    name = "curry rice"
    jpn = "カレーライス"
    image = "Curry-Rice.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "RICE VEGETABLES"
    description = "A favorite all over Hyrule, this simple dish has a flavor you just won't get tired of."
    return dictionary_builder(name, jpn, image, buff, category, description)


def dubious_food():
    name = "dubious food"
    jpn = "微妙な料理"
    image = "Dubious-Food.png"
    buff = "NONE"
    category = "OTHER"
    description = "It's too gross to even look at. A bizarre smell issues forth from this heap. Eating it won't hurt you though...probably."
    return dictionary_builder(name, jpn, image, buff, category, description)


def glazed_meat():
    name = "glazed meat"
    jpn = "甘露煮肉"
    image = "Glazed-Meat.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "MEAT"
    description = "The sweetness of the honey permeates the meat, giving it a complex taste profile."
    return dictionary_builder(name, jpn, image, buff, category, description)


def honey_candy():
    name = "honey candy"
    jpn = "ハチミツアメ"
    image = "Honey-Candy.png"
    buff = "NONE"
    category = "DESSERT"
    description = "A natural sweet, brimming with nutrition and made by stewing fresh honey."
    return dictionary_builder(name, jpn, image, buff, category, description)


def honeyed_apple():
    name = "honeyed apple"
    jpn = "ハチミツリンゴ"
    image = "Honeyed-Apple.png"
    buff = "NONE"
    category = "FRUITS DESSERT"
    description = "A natural sweet, brimming with nutrition and made by stewing fresh honey."
    return dictionary_builder(name, jpn, image, buff, category, description)


def fish_skewer():
    name = "fish skewer"
    jpn = "串焼き魚"
    image = "Fish-Skewer.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "SEAFOOD"
    description = "A simple dish made by cooking chunks of fresh fish on a skewer."
    return dictionary_builder(name, jpn, image, buff, category, description)


def copious_fish_skewers():
    name = "copious fish skewers"
    jpn = "山盛串焼き魚"
    image = "Copious-Fish-Skewers.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "SEAFOOD"
    description = "It's just a whole heap of stuff shoved on to a skewer, but it's still a pretty tasty dish."
    return dictionary_builder(name, jpn, image, buff, category, description)


def fish_mushroom_skewer():
    name = "fish & mushroom skewer"
    jpn = "串焼き魚キノコ添え"
    image = "Fish-and-Mushroom-Skewer.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "SEAFOOD"
    description = "A simple dish made by cooking skewered, fresh fish alongside fragrant mushrooms."
    return dictionary_builder(name, jpn, image, buff, category, description)


def fragrant_mushroom_saute():
    name = "fragrant mushroom sauté"
    jpn = "香りキノコ炒め"
    image = "Fragrant-Mushroom-Saute.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "VEGETABLES"
    description = "The fragrant aroma of this sautéed spice and mushroom dish makes your mouth water."
    return dictionary_builder(name, jpn, image, buff, category, description)


def fried_bananas():
    name = "fried bananas"
    jpn = "あげバナナ"
    image = "Fried-Bananas.png"
    buff = "MIGHTY"
    category = "VEGETABLES DESSERT"
    description = "Children love fried mighty bananas. The trick is frying them over very high heat."
    return dictionary_builder(name, jpn, image, buff, category, description)


def fried_egg_rice():
    name = "fried egg & rice"
    jpn = "目玉焼きライス"
    image = "Fried-Egg-and-Rice.png"
    buff = "NONE"
    category = "RICE"
    description = "The soft egg yolk pairs well with the fresh rice in this simple dish."
    return dictionary_builder(name, jpn, image, buff, category, description)


def fried_wild_greens():
    name = "fried wild greens"
    jpn = "焼き山菜"
    image = "Fried-Wild-Greens.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH NONE"
    category = "VEGETABLES"
    description = "A basic vegetable dish made by sautéing fresh wild plants."
    return dictionary_builder(name, jpn, image, buff, category, description)


def copious_fried_wild_greens():
    name = "copious fried wild greens"
    jpn = "山盛焼き山菜"
    image = "Copious-Fried-Wild-Greens.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH NONE"
    category = "VEGETABLES"
    description = "A healthy dish made by cooking mixed greens over a strong flame."
    return dictionary_builder(name, jpn, image, buff, category, description)


def fruit_mushroom_mix():
    name = "fruit & mushroom mix"
    jpn = "果実のキノコあえ"
    image = "Fruit-and-Mushroom-Mix.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH NONE"
    category = "VEGETABLES"
    description = "This dish contrasts the sweetness of fruit with the savoriness of mushrooms."
    return dictionary_builder(name, jpn, image, buff, category, description)


def fruit_pie():
    name = "fruit pie"
    jpn = "フルーツパイ"
    image = "Fruit-Pie.png"
    buff = "CHILLY ELECTRO HEARTY MIGHTY SPICY NONE"
    category = "FRUITS DESSERT"
    description = "A celebration isn't a celebration until this fruit-filled crust hits the table!"
    return dictionary_builder(name, jpn, image, buff, category, description)


def fruitcake():
    name = "fruitcake"
    jpn = "フルーツケーキ"
    image = "Fruitcake.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY NONE"
    category = "FRUITS DESSERT"
    description = "A celebration isn't a celebration until this fruit-filled crust hits the table!"
    return dictionary_builder(name, jpn, image, buff, category, description)


def glazed_mushrooms():
    name = "glazed mushrooms"
    jpn = "甘露煮キノコ"
    image = "Glazed-Mushrooms.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SPICY NONE"
    category = "VEGETABLES"
    description = "The honey in this mushroom dish gives it a sweet, complex taste and a savory finish."
    return dictionary_builder(name, jpn, image, buff, category, description)


def glazed_seafood():
    name = "glazed seasfood"
    jpn = "甘露煮魚"
    image = "Glazed-Seafood.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SPICY NONE"
    category = "SEAFOOD"
    description = "A seafood dish that you can actually wolf down whole!"
    return dictionary_builder(name, jpn, image, buff, category, description)


def glazed_veggies():
    name = "glazed veggies"
    jpn = "甘露煮野菜"
    image = "Glazed-Veggies.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SPICY NONE"
    category = "VEGETABLES"
    description = "Don't like the taste of vegetables? Simply sauté them in honey for a salty-sweet flavor!"
    return dictionary_builder(name, jpn, image, buff, category, description)


def gourmet_meat_rice_bowl():
    name = "gourmet meat & rice bowl"
    jpn = "極上ケモノ肉丼"
    image = "Gourmet-Meat-and-Rice-Bowl.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SPICY NONE"
    category = "MEAT RICE"
    description = "Only the most carefully selected cuts of high-quality meats go into this dish."
    return dictionary_builder(name, jpn, image, buff, category, description)


def gourmet_meat_seafood_fry():
    name = "gourmet meat & seafood fry"
    jpn = "山海焼き"
    image = "Gourmet-Meat-and-Seafood-Fry.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SPICY NONE"
    category = "MEAT SEAFOOD"
    description = "A marriage of the choicest cuts of meat and seafood. As delicious as it is filling!"
    return dictionary_builder(name, jpn, image, buff, category, description)


def gourmet_meat_curry():
    name = "gourmet meat curry"
    jpn = "極上肉カレー"
    image = "Gourmet-Meat-Curry.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SPICY"
    category = "MEAT RICE"
    description = "The high-quality meat used in this prized dish satisfies meat and curry lovers alike."
    return dictionary_builder(name, jpn, image, buff, category, description)


def gourmet_meat_stew():
    name = "gourmet meat stew"
    jpn = "極上肉シチュー"
    image = "Gourmet-Meat-Stew.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SPICY NONE"
    category = "MEAT SOUP"
    description = "The meat has simmered for so long it melts in your mouth. A true bucket-list meal!"
    return dictionary_builder(name, jpn, image, buff, category, description)


def gourmet_poultry_curry():
    name = "gourmet poultry curry"
    jpn = "極上チキンカレー"
    image = "Gourmet-Poultry-Curry.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SPICY NONE"
    category = "MEAT SOUP"
    description = "Once served in Hyrule Castle, the poultry used in this dish is of immensely high quality."
    return dictionary_builder(name, jpn, image, buff, category, description)


def gourmet_poultry_pilaf():
    name = "gourmet poultry pilaf"
    jpn = "極上チキンピラフ"
    image = "Gourmet-Poultry-Pilaf.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SPICY NONE"
    category = "MEAT RICE"
    description = "Made with the highest-quality poultry, every bite of this pilaf floods your mouth with flavor."
    return dictionary_builder(name, jpn, image, buff, category, description)


def gourmet_spiced_meat_skewer():
    name = "gourmet spiced meat skewer"
    jpn = "極上ケモノステーキ"
    image = "Gourmet-Spiced-Meat-Skewer.png"
    buff = "SPICY"
    category = "MEAT"
    description = "The rich aroma and juicy texture of this high-quality meat puts it in a league of its own."
    return dictionary_builder(name, jpn, image, buff, category, description)


def hard_boiled_egg():
    name = "hard-boiled egg"
    jpn = "ゆでタマゴ"
    image = "Hard-Boiled-Egg.png"
    buff = "NONE"
    category = "OTHER"
    description = "A bird egg boiled using water from naturally occurring hot springs. It's popular among children and is easy to make."
    return dictionary_builder(name, jpn, image, buff, category, description)


def herb_saute():
    name = "herb sauté"
    jpn = "甘露煮野菜"
    image = "Herb-Saute.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH NONE"
    category = "VEGETABLES"
    description = "A fragrant mixture of herbs and spices. It's easily recognized by its unique aroma."
    return dictionary_builder(name, jpn, image, buff, category, description)


def honey_crepe():
    name = "honey crêpe"
    jpn = "ハチミツクレープ"
    image = "Honey-Crepe.png"
    buff = "ENERGIZING NONE"
    category = "DESSERT"
    description = "Honey has been drizzled over thin crepes to bring out their natural sweetness and flavor."
    return dictionary_builder(name, jpn, image, buff, category, description)


def honeyed_fruits():
    name = "honeyed fruits"
    jpn = "ハチミツ果実"
    image = "Honeyed-Fruits.png"
    buff = "ENERGIZING NONE"
    category = "FRUITS DESSERT"
    description = "A dish that combines the thick sweetness of honey with the acidity of sour fruits."
    return dictionary_builder(name, jpn, image, buff, category, description)


def hot_buttered_apple():
    name = "hot buttered apple"
    jpn = "リンゴバター"
    image = "Hot-Buttered-Apple.png"
    buff = "ENERGIZING NONE"
    category = "FRUITS DESSERT"
    description = "The apple's sweetness has been enhanced by smothering it with butter and baking it."
    return dictionary_builder(name, jpn, image, buff, category, description)


def mabe_souffle():
    name = "mabe soufflé"
    jpn = "メーベスフレ"
    image = "Mabe-Souffle.png"
    buff = "NONE"
    category = "OTHER"
    description = "A soufflé made with farm-fresh milk, eggs, and butter. This Mabe Village treat is garnished with some Hyrule herb."
    return dictionary_builder(name, jpn, image, buff, category, description)


def meat_mushroom_skewer():
    name = "meat & mushroom skewer"
    jpn = "串焼き肉キノコ添え"
    image = "Meat-and-Mushroom-Skewer.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SPICY NONE"
    category = "MEAT"
    description = "A filling dish made by grilling various mountain ingredients with either Steak or Bird Meat."
    return dictionary_builder(name, jpn, image, buff, category, description)


def meat_rice_bowl():
    name = "meat & rice bowl"
    jpn = "ケモノ肉丼"
    image = "Meat-and-Rice-Bowl.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH NONE"
    category = "MEAT RICE"
    description = "This dish of rice and lightly seared meat is a mainstay all throughout Hyrule."
    return dictionary_builder(name, jpn, image, buff, category, description)


def meat_seafood_fry():
    name = "meat & seafood fry"
    jpn = "山海焼き"
    image = "Meat-and-Seafood-Fry.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH NONE"
    category = "MEAT SEAFOOD"
    description = "A filling dish made by cooking fresh seafood and meat together."
    return dictionary_builder(name, jpn, image, buff, category, description)


def meat_curry():
    name = "meat curry"
    jpn = "ケモノ肉カレー"
    image = "Meat-Curry.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH NONE"
    category = "MEAT"
    description = "The heat from the spice allows you to enjoy the large portion of the meat's savoriness."
    return dictionary_builder(name, jpn, image, buff, category, description)


def meat_pie():
    name = "meat pie"
    jpn = "ミートパイ"
    image = "Meat-Pie.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH NONE"
    category = "MEAT"
    description = "You'll need an extra napkin to deal with this juicy pie of perfectly baked minced meat."
    return dictionary_builder(name, jpn, image, buff, category, description)


def meat_skewer():
    name = "meat skewer"
    jpn = "串焼き肉"
    image = "Meat-Skewer.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH NONE"
    category = "MEAT"
    description = "A juicy, filling snack made by grilling small chunks of meat on a skewer."
    return dictionary_builder(name, jpn, image, buff, category, description)


def copious_meat_skewer():
    name = "copious meat skewers"
    jpn = "山盛串焼き肉"
    image = "Copious-Meat-Skewers.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH NONE"
    category = "MEAT"
    description = "Just shove a bunch of meat on to a skewer and you're good to go."
    return dictionary_builder(name, jpn, image, buff, category, description)


def meat_stew():
    name = "meat stew"
    jpn = "肉シチュー"
    image = "Meat-Stew.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH NONE"
    category = "MEAT SOUP"
    description = "The hearty meat in this mainstay dish leaves bellies satisfied all throughout Hyrule."
    return dictionary_builder(name, jpn, image, buff, category, description)


def meat_stuffed_pumpkin():
    name = "meat stuffed pumpkin"
    jpn = "肉詰めカボチャ"
    image = "Meat-Stuffed-Pumpkin.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH NONE"
    category = "MEAT SOUP"
    description = "This hollow, meat-filled fortified pumpkin is a local specialty of Kakariko Village."
    return dictionary_builder(name, jpn, image, buff, category, description)


def meaty_rice_balls():
    name = "meaty rice balls"
    jpn = "肉おにぎり"
    image = "Meaty-Rice-Balls.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH NONE"
    category = "MEAT RICE"
    description = "The sweet and spicy meat stuffed into these rice balls will keep you full for some time."
    return dictionary_builder(name, jpn, image, buff, category, description)


def monster_cake():
    name = "monster cake"
    jpn = "マモノケーキ"
    image = "Monster-Cake.png"
    buff = "NONE"
    category = "MONSTER DESSERT"
    description = "It's said that once you have a taste of this cake, you'll never forget its sweetness."
    return dictionary_builder(name, jpn, image, buff, category, description)


def monster_curry():
    name = "monster curry"
    jpn = "マモノカレー"
    image = "Monster-Curry.png"
    buff = "NONE"
    category = "MONSTER RICE"
    description = "This unusual take on curry uses monster extract and doesn't rely on spices."
    return dictionary_builder(name, jpn, image, buff, category, description)


def monster_rice_balls():
    name = "monster rice balls"
    jpn = "マモノにぎり"
    image = "Monster-Rice-Balls.png"
    buff = "NONE"
    category = "MONSTER RICE"
    description = "Rice balls flavored with monster extract. Their unique aroma is not for everyone."
    return dictionary_builder(name, jpn, image, buff, category, description)


def monster_soup():
    name = "monster soup"
    jpn = "マモノスープ"
    image = "Monster-Soup.png"
    buff = "NONE"
    category = "MONSTER SOUP"
    description = "Using monster extract as a base, this soup's distinct gaminess is either loved or hated."
    return dictionary_builder(name, jpn, image, buff, category, description)


def monster_stew():
    name = "monster stew"
    jpn = "マモノカレー"
    image = "Monster-Stew.png"
    buff = "NONE"
    category = "MONSTER SOUP"
    description = "Meat and seafood simmered in monster extract. A savory dish despite its ingredients."
    return dictionary_builder(name, jpn, image, buff, category, description)


def mushroom_omelet():
    name = "mushroom omelet"
    jpn = "キノコオムレツ"
    image = "Mushroom-Omelet.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SPICY NONE"
    category = "VEGETABLES"
    description = "The fluffy texture of this omelet is one of the great joys of this dish, as well as life."
    return dictionary_builder(name, jpn, image, buff, category, description)


def mushroom_rice_balls():
    name = "mushroom rice balls"
    jpn = "キノコおにぎり"
    image = "Mushroom-Rice-Balls.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SPICY NONE"
    category = "VEGETABLES RICE"
    description = "The aroma of the mushrooms tickles your nose as you peel back the leafy wrapping."
    return dictionary_builder(name, jpn, image, buff, category, description)


def mushroom_risotto():
    name = "mushroom risotto"
    jpn = "キノコリゾット"
    image = "Mushroom-Risotto.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SPICY NONE"
    category = "VEGETABLES RICE"
    description = "The tantalizing aroma of mushrooms and butter beckons you to the table."
    return dictionary_builder(name, jpn, image, buff, category, description)


def mushroom_skewer():
    name = "mushroom skewer"
    jpn = "串焼きキノコ"
    image = "Mushroom-Skewer.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SPICY NONE"
    category = "VEGETABLES"
    description = "This simple mushroom-packed skewer has its colorful presentation to thank for its appeal."
    return dictionary_builder(name, jpn, image, buff, category, description)


def copious_mushroom_skewers():
    name = "copious-mushroom skewers"
    jpn = "山盛串焼きキノコ"
    image = "Copious-Mushroom-Skewers.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SPICY NONE"
    category = "VEGETABLES"
    description = "Fans of fungal cuisine can't resist this simple mushroom-skewer dish. Very filling."
    return dictionary_builder(name, jpn, image, buff, category, description)


def noble_pursuit():
    name = "noble pursuit"
    jpn = "ヴァーイミーツヴォーイ"
    image = "Noble-Pursuit.png"
    buff = "MIGHTY"
    category = "OTHER"
    description = "The Noble Canteen's most famous drink...or an iced tropical-juice mixture that does it justice."
    return dictionary_builder(name, jpn, image, buff, category, description)


def nutcake():
    name = "nutcake"
    jpn = "ナッツケーキ"
    image = "Nutcake.png"
    buff = "NONE"
    category = "DESSERT"
    description = "Forest nuts give this cake a pleasant texture and a simple, understated sweetness."
    return dictionary_builder(name, jpn, image, buff, category, description)


def omelet():
    name = "omelet"
    jpn = "卵焼き"
    image = "Omelet.png"
    buff = "NONE"
    category = "OTHER"
    description = "This simple dish is common all over Hyrule. Simply fry egg until it's nice and plump."
    return dictionary_builder(name, jpn, image, buff, category, description)


def pepper_seafood():
    name = "pepper seafood"
    jpn = "スパイシー焼き魚"
    image = "Pepper-Seafood.png"
    buff = "SPICY"
    category = "SEAFOOD"
    description = "The pepper seeds grilled with this seafood draw out its taste and pleasant aroma."
    return dictionary_builder(name, jpn, image, buff, category, description)


def pepper_steak():
    name = "pepper steak"
    jpn = "スパイシー焼き魚"
    image = "Pepper-Steak.png"
    buff = "SPICY"
    category = "MEAT"
    description = "A dish made by cooking meat in crushed peppers, suppressing the gamy taste while accentuating its flavor."
    return dictionary_builder(name, jpn, image, buff, category, description)


def plain_crepe():
    name = "plain crêpe"
    jpn = "プレーンクレープ"
    image = "Plain-Crepe.png"
    buff = "NONE"
    category = "DESSERT"
    description = "The simplicity of this dish lets the flavor of its ingredients shine."
    return dictionary_builder(name, jpn, image, buff, category, description)


def porgy_meuniere():
    name = "porgy meunière"
    jpn = "鯛ムニエル"
    image = "Porgy-Meuniere.png"
    buff = "MIGHTY TOUGH"
    category = "SEAFOOD"
    description = "Popular among residents of coastal regions, this juicy porgy is a delish dish."
    return dictionary_builder(name, jpn, image, buff, category, description)


def poultry_curry():
    name = "poultry curry"
    jpn = "チキンカレー"
    image = "Poultry-Curry.png"
    buff = "SPICY"
    category = "MEAT RICE"
    description = "The savory meat pairs well with the aroma of spice in this common curry."
    return dictionary_builder(name, jpn, image, buff, category, description)


def poultry_pilaf():
    name = "poultry pilaf"
    jpn = "チキンピラフ"
    image = "Poultry-Pilaf.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "MEAT RICE"
    description = "Sautéed Hylian rice steamed in poultry broth. Cook on low heat until the rice is fluffy."
    return dictionary_builder(name, jpn, image, buff, category, description)


def prime_meat_rice_bowl():
    name = "prime meat & rice bowl"
    jpn = "上ケモノ肉丼"
    image = "Prime-Meat-and-Rice-Bowl.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "MEAT RICE"
    description = "This bowl is loaded with high-quality meat. Your hunt for a serious meal ends here."
    return dictionary_builder(name, jpn, image, buff, category, description)


def prime_meat_seafood_fry():
    name = "prime meat & seafood fry"
    jpn = "上山海焼き"
    image = "Prime-Meat-and-Seafood-Fry.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "MEAT SEAFOOD"
    description = "This comfort dish is made with choice cuts of meat and seafood."
    return dictionary_builder(name, jpn, image, buff, category, description)


def prime_meat_curry():
    name = "prime meat curry"
    jpn = "上肉カレー"
    image = "Prime-Meat-Curry.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "MEAT"
    description = "The high-quality meat in this curry has given it a deeper taste than most other curries."
    return dictionary_builder(name, jpn, image, buff, category, description)


def prime_meat_stew():
    name = "prime meat stew"
    jpn = "上肉シチュー"
    image = "Prime-Meat-Stew.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "MEAT SOUP"
    description = "Letting the large portions of choice cuts of meat simmer brought out their savoriness."
    return dictionary_builder(name, jpn, image, buff, category, description)


def prime_poultry_curry():
    name = "prime poultry curry"
    jpn = "上チキンカレー"
    image = "Prime-Poultry-Curry.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "MEAT RICE"
    description = "The secret to this curry's flavor is taking it off the heat while you add the spices."
    return dictionary_builder(name, jpn, image, buff, category, description)


def prime_poultry_pilaf():
    name = "prime poultry pilaf"
    jpn = "上チキンピラフ"
    image = "Prime-Poultry-Pilaf.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "MEAT RICE"
    description = "The rice permeates the savory taste of the poultry in this Gerudo-region favorite."
    return dictionary_builder(name, jpn, image, buff, category, description)


def prime_spiced_meat_skewer():
    name = "prime spiced meat skewer"
    jpn = "上ケモノステーキ"
    image = "Prime-Spiced-Meat-Skewer.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "MEAT"
    description = "The simple preparation of this steak dish belies its complex taste profile."
    return dictionary_builder(name, jpn, image, buff, category, description)


def pumpkin_pie():
    name = "pumpkin pie"
    jpn = "カボチャケーキ"
    image = "Pumpkin-Pie.png"
    buff = "TOUGH"
    category = "DESSERT"
    description = "The intense sweetness of fortified pumpkins makes this dessert popular among children."
    return dictionary_builder(name, jpn, image, buff, category, description)


def pumpkin_stew():
    name = "pumpkin stew"
    jpn = "カボチャシチュー"
    image = "Pumpkin-Stew.png"
    buff = "TOUGH"
    category = "SOUP"
    description = "Simply simmer a fortified pumpkin to make this dish. A favorite in Kakariko Village."
    return dictionary_builder(name, jpn, image, buff, category, description)


def rock_hard_food():
    name = "rock-hard food"
    jpn = "硬すぎ料理"
    image = "Rock-Hard-Food.png"
    buff = "NONE"
    category = "OTHER"
    description = "A dish gone awry after adding the wrong ingredient. Chewing your way through this won't be fun, but it will fill you up when you're between a rock and a hard place."
    return dictionary_builder(name, jpn, image, buff, category, description)


def salmon_meuniere():
    name = "salmon meunière"
    jpn = "サーモンムニエル"
    image = "Salmon-Meuniere.png"
    buff = "HEARTY"
    category = "SEAFOOD"
    description = "The crispy skin of this fried hearty salmon puts its texture in a class all its own."
    return dictionary_builder(name, jpn, image, buff, category, description)


def salmon_risotto():
    name = "salmon risotto"
    jpn = "サーモンリゾット"
    image = "Salmon-Risotto.png"
    buff = "HEARTY"
    category = "SEAFOOD"
    description = "The rice used in this rich risotto permeates the light flavor of the salmon."
    return dictionary_builder(name, jpn, image, buff, category, description)


def salt_grilled_crab():
    name = "salt-grilled crab"
    jpn = "岩塩焼きガニ"
    image = "Salt-Grilled-Crab.png"
    buff = "NONE MIGHTY TOUGH ENERGIZING"
    category = "SEAFOOD"
    description = "Nine out of ten fishermen agree: crab is best enjoyed grilled and with just a bit of salt."
    return dictionary_builder(name, jpn, image, buff, category, description)


def salt_grilled_fish():
    name = "salt-grilled fish"
    jpn = "塩焼き魚"
    image = "Salt-Grilled-Fish.png"
    buff = "NONE CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "SEAFOOD"
    description = "A simple dish made by rolling a whole fish in natural rock salt before grilling it."
    return dictionary_builder(name, jpn, image, buff, category, description)


def salt_grilled_gourmet_meat():
    name = "salt-grilled gourmet meat"
    jpn = "極上岩塩焼き肉"
    image = "Salt-Grilled-Gourmet-Meat.png"
    buff = "NONE CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "MEAT"
    description = "This lavish grilled dish makes liberal use of high-quality cuts of meat."
    return dictionary_builder(name, jpn, image, buff, category, description)


def salt_grilled_greens():
    name = "salt-grilled greens"
    jpn = "塩焼き山菜"
    image = "Salt-Grilled-Greens.png"
    buff = "NONE CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "VEGETABLES"
    description = "A health-boosting dish made with leafy greens and a touch of salt."
    return dictionary_builder(name, jpn, image, buff, category, description)


def salt_grilled_meat():
    name = "salt-grilled meat"
    jpn = "岩塩焼き肉"
    image = "Salt-Grilled-Meat.png"
    buff = "NONE CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "MEAT"
    description = "Short on ingredients? Just rub some meat in salt and cook it for a simple, tasty dish."
    return dictionary_builder(name, jpn, image, buff, category, description)


def salt_grilled_mushrooms():
    name = "salt-grilled mushrooms"
    jpn = "塩焼きキノコ"
    image = "Salt-Grilled-Mushrooms.png"
    buff = "NONE CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "VEGETABLES"
    description = "A basic mushroom dish made by lightly salting mushrooms and grilling them."
    return dictionary_builder(name, jpn, image, buff, category, description)


def salt_grilled_prime_meat():
    name = "salt-grilled prime meat"
    jpn = "上岩塩焼き肉"
    image = "Salt-Grilled-Prime-Meat.png"
    buff = "NONE CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "MEAT"
    description = "A simple yet exquisite dish made by grilling high-quality meat on top of rock salt."
    return dictionary_builder(name, jpn, image, buff, category, description)


def sauteed_nuts():
    name = "sautéed nuts"
    jpn = "ナッツ炒め"
    image = "Sauteed-Nuts.png"
    buff = "NONE"
    description = "These sautéed tree seeds are the perfect snack for the busy adventurer on the go!"
    category = "OTHER"
    return dictionary_builder(name, jpn, image, buff, category, description)


def seafood_curry():
    name = "seafood curry"
    jpn = "海の幸カレー"
    image = "Seafood-Curry.png"
    buff = "HEARTY MIGHTY TOUGH"
    description = "This dish brims with treasures from the sea. Its spice packs a kick, so it's not for kids."
    category = "SEAFOOD RICE"
    return dictionary_builder(name, jpn, image, buff, category, description)


def seafood_fried_rice():
    name = "seafood fried rice"
    jpn = "海鮮チャーハン"
    image = "Seafood-Fried-Rice.png"
    buff = "HEARTY MIGHTY TOUGH"
    description = "Various seafood has been sautéed with rice. The stronger the flame, the tastier the dish!"
    category = "SEAFOOD RICE"
    return dictionary_builder(name, jpn, image, buff, category, description)


def seafood_meuniere():
    name = "seafood meunière"
    jpn = "魚ムニエル"
    image = "Seafood-Meuniere.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY SNEAKY SPICY"
    category = "SEAFOOD"
    description = "Rich butter flanks fresh seafood. The secret ingredient is lots and lots of love."
    return dictionary_builder(name, jpn, image, buff, category, description)


def seafood_paella():
    name = "seafood paella"
    jpn = "海鮮パエリア"
    image = "Seafood-Paella.png"
    buff = "HEARTY MIGHTY TOUGH"
    category = "SEAFOOD RICE"
    description = "No fisherman's birthday bash would be complete without this top-shelf seafood dish."
    return dictionary_builder(name, jpn, image, buff, category, description)


def seafood_rice_balls():
    name = "seafood rice balls"
    jpn = "海鮮おにぎり"
    image = "Seafood-Rice-Balls.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY SNEAKY SPICY"
    category = "SEAFOOD RICE"
    description = "Stuffed with aromatic seafood, the flavor can vary by ingredients but never disappoints."
    return dictionary_builder(name, jpn, image, buff, category, description)


def seafood_skewer():
    name = "seafood skewer"
    jpn = "魚貝串焼き"
    image = "Seafood-Skewer.png"
    buff = "ENDURING ENERGIZING HEARTY MIGHTY TOUGH"
    category = "SEAFOOD"
    description = "The natural water in this medley of seafaring creatures makes for a delicious broth."
    return dictionary_builder(name, jpn, image, buff, category, description)


def simmered_fruit():
    name = "simmered fruit"
    jpn = "煮込み果実"
    image = "Simmered-Fruit.png"
    buff = "NONE CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "FRUITS"
    description = "This sweet dish is made by heaping tasty fruits into a pan and simmering until tender."
    return dictionary_builder(name, jpn, image, buff, category, description)


def copious_simmered_fruit():
    name = "copious simmered fruit"
    jpn = "山盛煮込み果実"
    image = "Copious-Simmered-Fruit.png"
    buff = "NONE CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "FRUITS"
    description = "The flavors of the various fruits in this simmered dish exist in perfect harmony."
    return dictionary_builder(name, jpn, image, buff, category, description)


def steamed_fish():
    name = "steamed fish"
    jpn = "包み焼き魚"
    image = "Steamed-Fish.png"
    buff = "NONE CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "SEAFOOD"
    description = "A refined dish made by wrapping a fresh fish in fragrant wild greens and cooking it."
    return dictionary_builder(name, jpn, image, buff, category, description)


def steamed_fruit():
    name = "steamed fruit"
    jpn = "蒸し焼き果実"
    image = "Steamed-Fruit.png"
    buff = "NONE CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "FRUITS"
    description = "A regional dish made by steaming near-ripened fruits in the leaves of fragrant plants."
    return dictionary_builder(name, jpn, image, buff, category, description)


def steamed_meat():
    name = "steamed meat"
    jpn = "包み焼き肉"
    image = "Steamed-Meat.png"
    buff = "NONE CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "MEAT"
    description = "This meat dish has been wrapped in fragrant leaves and steamed to preserve its moisture."
    return dictionary_builder(name, jpn, image, buff, category, description)


def steamed_mushrooms():
    name = "steamed mushrooms"
    jpn = "包み焼きキノコ"
    image = "Steamed-Mushrooms.png"
    buff = "NONE CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "VEGETABLES"
    description = "A healthy vegetable dish achieved by steaming mushrooms in plant leaves."
    return dictionary_builder(name, jpn, image, buff, category, description)


def tabantha_bake():
    name = "tabantha bake"
    jpn = "タバンタ焼き"
    image = "Tabantha-Bake.png"
    buff = "HASTY"
    category = "OTHER"
    description = "A warming dish from Tabantha Village made by wrapping mushrooms in bread dough, then baking."
    return dictionary_builder(name, jpn, image, buff, category, description)


def veggie_cream_soup():
    name = "veggie cream soup"
    jpn = "ニンジンシチュー"
    image = "Veggie-Cream-Soup.png"
    buff = "NONE CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "SOUP VEGETABLES"
    description = "This creamy soup showcases the sweetness of vegetables in a veritable taste explosion."
    return dictionary_builder(name, jpn, image, buff, category, description)


def vegetable_curry():
    name = "Vegetable curry"
    jpn = "	野菜カレー"
    image = "Vegetable-Curry.png"
    buff = "NONE CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "SOUP VEGETABLES"
    description = "This healthy curry is popular for its mild flavor and moderate spiciness."
    return dictionary_builder(name, jpn, image, buff, category, description)


def vegetable_omelet():
    name = "vegetable omelet"
    jpn = "	野菜オムレツ"
    image = "Vegetable-Omelet.png"
    buff = "NONE CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH HASTY"
    category = "VEGETABLES"
    description = "This home-style dish mixes fluffy eggs with chopped vegetables for nutritional balance."
    return dictionary_builder(name, jpn, image, buff, category, description)


def vegetable_risotto():
    name = "vegetable risotto"
    jpn = "	野菜リゾット"
    image = "Vegetable-Risotto.png"
    buff = "NONE CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "RICE VEGETABLES"
    description = "The sweetness of the ingredients gives this risotto a mild flavor."
    return dictionary_builder(name, jpn, image, buff, category, description)


def veggie_rice_balls():
    name = "veggie rice balls"
    jpn = "	山菜おにぎり"
    image = "Veggie-Rice-Balls.png"
    buff = "NONE CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SNEAKY SPICY TOUGH"
    category = "RICE VEGETABLES"
    description = "This home-style dish of Kakariko Village is stuffed with the bounty of the mountains."
    return dictionary_builder(name, jpn, image, buff, category, description)


def warm_milk():
    name = "warm milk"
    jpn = "ホットミルク"
    image = "Warm-Milk.png"
    buff = "CHILLY ELECTRO ENDURING ENERGIZING HASTY HEARTY MIGHTY SPICY NONE"
    category = "OTHER"
    description = "Make this by heating up some milk. Drink it before bed to ensure a good night's sleep."
    return dictionary_builder(name, jpn, image, buff, category, description)


def wheat_bread():
    name = "wheat bread"
    jpn = "小麦パン"
    image = "Wheat-Bread.png"
    buff = "NONE"
    category = "OTHER"
    description = "Made with wheat from the Tabantha region, this soft, springy bread smells just heavenly."
    return dictionary_builder(name, jpn, image, buff, category, description)


def wildberry_crepe():
    name = "wildberry crêpe"
    jpn = "イチゴクレープ"
    image = "Wildberry-Crepe.png"
    buff = "NONE"
    category = "FRUITS DESSERT"
    description = "This creamy soup showcases the sweetness of vegetables in a veritable taste explosion."
    return dictionary_builder(name, jpn, image, buff, category, description)


def recipe_data():
    rows = [
        apple_pie(), carrot_cake(), ceremonial_platter(), clam_chowder(),
        deya_hot_pot(), egg_pudding(), egg_tart(), fish_pie(), carrot_stew(),
        crab_omelet_with_rice(), crab_risotto(), crab_stir_fry(),
        cream_of_mushroom(), cream_of_vegetable_soup(), creamy_heart_soup(),
        creamy_meat_soup(), creamy_seafood_soup(), curry_pilaf(), curry_rice(),
        dubious_food(), glazed_meat(), honey_candy(), honeyed_apple(),
        fish_skewer(), copious_fish_skewers(), fish_mushroom_skewer(),
        fragrant_mushroom_saute(), fried_bananas(), fried_egg_rice(),
        fried_wild_greens(), copious_fried_wild_greens(), fruit_mushroom_mix(),
        fruit_pie(), fruitcake(), glazed_mushrooms(), glazed_seafood(),
        glazed_veggies(), gourmet_meat_rice_bowl(), gourmet_meat_seafood_fry(),
        gourmet_meat_curry(), gourmet_meat_stew(), gourmet_poultry_curry(),
        gourmet_poultry_pilaf(), gourmet_spiced_meat_skewer(), hard_boiled_egg(),
        herb_saute(), honey_crepe(), honeyed_fruits(), hot_buttered_apple(),
        mabe_souffle(), meat_mushroom_skewer(), meat_rice_bowl(),
        meat_seafood_fry(), meat_curry(), meat_pie(), meat_skewer(),
        copious_meat_skewer(), meat_stew(), meat_stuffed_pumpkin(),
        meaty_rice_balls(), monster_cake(), monster_curry(), monster_rice_balls(),
        monster_soup(), monster_stew(), mushroom_omelet(), mushroom_rice_balls(),
        mushroom_risotto(), mushroom_skewer(), copious_mushroom_skewers(),
        noble_pursuit(), nutcake(), omelet(), pepper_seafood(),
        pepper_steak(), plain_crepe(), porgy_meuniere(), poultry_curry(),
        poultry_pilaf(), prime_meat_rice_bowl(), prime_meat_seafood_fry(),
        prime_meat_curry(), prime_meat_stew(), prime_poultry_curry(),
        prime_poultry_pilaf(), prime_spiced_meat_skewer(), pumpkin_pie(),
        pumpkin_stew(), rock_hard_food(), salmon_meuniere(), salmon_risotto(),
        salt_grilled_crab(), salt_grilled_fish(), salt_grilled_gourmet_meat(),
        salt_grilled_greens(), salt_grilled_meat(), salt_grilled_mushrooms(),
        salt_grilled_prime_meat(), sauteed_nuts(), seafood_curry(),
        seafood_meuniere(), seafood_paella(), seafood_rice_balls(),
        seafood_skewer(), simmered_fruit(), copious_simmered_fruit(),
        steamed_fish(), steamed_fruit(), steamed_meat(), steamed_meat(),
        steamed_mushrooms(), tabantha_bake(), veggie_cream_soup(),
        vegetable_curry(), vegetable_omelet(), vegetable_risotto(),
        veggie_rice_balls(), warm_milk(), wheat_bread(), wildberry_crepe()
    ]

    # list of recipes requires all keys
    for row in rows:
        # keys added to contain all filters for row
        row['keys'] = row["buff"] + " " + row["category"]

    # list of recipes requires BUFF and CATEGORY unique data filters
    buff = {"key": "buff", "data": [], "default": "NONE"}
    category = {"key": "category", "data": [], "default": "OTHER"}
    filters = [buff, category]
    # build data filters for "key" values in each row of filters
    for data_filter in filters:
        temp_list = []  # data filter work list
        for row in rows:  # go through list/data row by row
            keys = row[data_filter["key"]].split()
            for key in keys:  # review each key
                if key.lower() != data_filter["default"].lower():
                    temp_list.append(key)  # add key if NOT default
        # make list unique and sort
        temp_list = list(set(temp_list))  # set/tuple is unique
        temp_list.sort()
        # add default key at front
        temp_list.insert(0, data_filter["default"])
        # set the permanent data filter
        data_filter["data"] = temp_list

    return rows, filters
