def generate_diet_plan(glucose, blood_pressure, bmi, language='en'):
    """Generate personalized diet plan based on health metrics."""
    
    # Determine risk levels
    sugar_high = glucose >= 126
    sugar_pre = 100 <= glucose < 126
    bp_high = blood_pressure >= 90
    overweight = bmi >= 25
    obese = bmi >= 30
    
    plans = {
        'en': {
            'foods_to_eat': [],
            'foods_to_avoid': [],
            'breakfast': [],
            'lunch': [],
            'dinner': [],
            'snacks': [],
            'tips': [],
            'water_intake': '8-10 glasses per day',
            'exercise': '30 minutes walking daily',
        }
    }
    
    plan = plans['en']
    
    # Base healthy foods
    plan['foods_to_eat'] = [
        '🥦 Green leafy vegetables (spinach, kale, broccoli)',
        '🐟 Lean proteins (fish, chicken, tofu)',
        '🫐 Low glycemic fruits (berries, apple, pear)',
        '🌾 Whole grains (quinoa, oats, brown rice)',
        '🥜 Nuts and seeds (almonds, flaxseeds, chia)',
        '🫒 Healthy fats (olive oil, avocado)',
        '🧄 Garlic and onion (blood sugar regulation)',
        '🫘 Legumes (lentils, chickpeas, black beans)',
    ]
    
    plan['foods_to_avoid'] = [
        '🍬 Sugary drinks and sodas',
        '🍞 White bread and refined flour products',
        '🍟 Deep fried and fast foods',
        '🍰 Cakes, pastries, and sweets',
        '🧂 Excessive salt and processed foods',
        '🥩 Red meat and fatty cuts',
        '🍺 Alcohol and carbonated beverages',
        '🧁 Packaged snacks and cookies',
    ]
    
    # Customize based on glucose
    if sugar_high:
        plan['breakfast'] = [
            '🥣 Steel-cut oats with cinnamon (no sugar) + handful almonds',
            '🥚 2 boiled eggs + cucumber slices + green tea (no sugar)',
            '🥑 Avocado toast on whole grain bread + black coffee',
        ]
        plan['lunch'] = [
            '🍛 Grilled chicken with steamed vegetables and quinoa',
            '🥗 Large mixed salad with olive oil dressing + lentil soup',
            '🐟 Baked salmon with brown rice and broccoli',
        ]
        plan['dinner'] = [
            '🍲 Dal (lentil curry) with 1 chapati + vegetable sabzi',
            '🥣 Vegetable soup + small portion of whole grain bread',
            '🐟 Grilled fish with steamed spinach and cucumber raita',
        ]
        plan['tips'] = [
            '⏰ Eat meals at fixed times every day',
            '🍽️ Use smaller plates to control portions',
            '🚶 Walk for 10 minutes after each meal',
            '📊 Monitor blood sugar before and after meals',
            '🚫 Never skip breakfast — it stabilizes blood sugar',
            '💧 Drink a glass of water before every meal',
        ]
    elif sugar_pre:
        plan['breakfast'] = [
            '🥣 Oatmeal with berries and a sprinkle of flaxseeds',
            '🥚 Vegetable omelette with whole grain toast',
            '🥛 Greek yogurt with apple slices and walnuts',
        ]
        plan['lunch'] = [
            '🥗 Mixed bean salad with lots of vegetables',
            '🍗 Grilled chicken wrap in whole wheat tortilla',
            '🍲 Sambar with brown rice and vegetable curry',
        ]
        plan['dinner'] = [
            '🥦 Stir-fried vegetables with tofu or paneer',
            '🍲 Lentil soup with 2 whole wheat chapatis',
            '🐟 Baked fish with roasted vegetables',
        ]
        plan['tips'] = [
            '📉 Reduce carbohydrate portions gradually',
            '🏃 Aim for 150 minutes of exercise per week',
            '🌿 Include bitter gourd (karela) in diet',
            '📅 Get HbA1c tested every 3 months',
        ]
    else:
        plan['breakfast'] = [
            '🥣 Muesli with low-fat milk and fresh fruits',
            '🥞 Whole wheat pancakes with honey and berries',
            '🥚 Scrambled eggs with vegetables and toast',
        ]
        plan['lunch'] = [
            '🍛 Balanced thali with rice, dal, vegetable sabzi',
            '🥗 Grilled chicken salad with whole grain bread',
            '🍜 Vegetable pulao with raita and pickle',
        ]
        plan['dinner'] = [
            '🍲 Dal makhani with 2 chapatis and salad',
            '🐟 Fish curry with brown rice',
            '🥗 Mixed vegetable sabzi with paneer and chapatis',
        ]
        plan['tips'] = [
            '✅ Maintain current healthy habits',
            '🏊 Regular exercise 4-5 times per week',
            '🍎 5 servings of fruits and vegetables daily',
            '😴 Get 7-8 hours of quality sleep',
        ]
    
    # BP-specific additions
    if bp_high:
        plan['foods_to_avoid'].append('🧂 Pickles, papad, and salty snacks')
        plan['foods_to_avoid'].append('🥫 Canned and preserved foods')
        plan['tips'].append('🧂 Limit sodium to less than 1500mg per day')
        plan['tips'].append('🍌 Eat potassium-rich foods (banana, spinach)')
        plan['foods_to_eat'].append('🍌 Potassium-rich foods (banana, sweet potato)')
    
    # BMI-specific additions
    if obese:
        plan['tips'].append('⚖️ Aim to lose 0.5-1 kg per week gradually')
        plan['tips'].append('🥤 Avoid liquid calories (juices, milk tea)')
        plan['foods_to_eat'].append('🥒 Cucumber and celery (low-calorie snacks)')
        plan['snacks'] = ['🥜 10 almonds + green tea', '🍎 1 apple', '🥒 Cucumber with hummus', '🥛 Low-fat yogurt']
    elif overweight:
        plan['tips'].append('🥗 Increase vegetable portions, reduce grain portions')
        plan['snacks'] = ['🥜 Handful of mixed nuts', '🍐 1 pear or apple', '🥕 Carrot sticks with hummus']
    else:
        plan['snacks'] = ['🥜 Mixed nuts', '🍌 Banana with peanut butter', '🥛 Greek yogurt', '🍎 Fresh fruits']
    
    # Add multilingual labels
    if language == 'te':  # Telugu
        plan['lang_note'] = 'మీ ఆహార ప్రణాళిక (Your Diet Plan)'
        plan['morning_label'] = 'అల్పాహారం (Breakfast)'
        plan['lunch_label'] = 'మధ్యాహ్న భోజనం (Lunch)'
        plan['dinner_label'] = 'రాత్రి భోజనం (Dinner)'
    elif language == 'hi':  # Hindi
        plan['lang_note'] = 'आपकी आहार योजना (Your Diet Plan)'
        plan['morning_label'] = 'नाश्ता (Breakfast)'
        plan['lunch_label'] = 'दोपहर का खाना (Lunch)'
        plan['dinner_label'] = 'रात का खाना (Dinner)'
    else:
        plan['lang_note'] = 'Your Personalized Diet Plan'
        plan['morning_label'] = 'Breakfast'
        plan['lunch_label'] = 'Lunch'
        plan['dinner_label'] = 'Dinner'
    
    plan['glucose_level'] = glucose
    plan['bp_level'] = blood_pressure
    plan['bmi_value'] = bmi
    
    return plan
