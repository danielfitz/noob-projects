#! python3
# 

import random, os

questionnaire = {'All activity guides can be found online.': 'No.',
 'Are you an only child?': 'No.',
 'Are you new to our school?': 'Yes.',
 'Can you do a magic trick?': 'No.',
 'Can you name something you hate to eat?': 'No.',
 'Can you remember when you were a baby?': 'No.',
 'Can you roll both sides of your tongue up?': 'No.',
 'Can you stand on your head?': 'No.',
 'Can you think of three words that rhyme?': 'No.',
 'Can you touch your tongue to your nose?': 'Yes.',
 'Can you whistle?': 'No.',
 'Can you wiggle your ears?': 'Yes.',
 'Did the doctor ever give you a shot?': 'Yes.',
 'Did you ever climb a tree?': 'No.',
 'Did you ever fall asleep while riding in a car?': 'No.',
 'Did you ever fall out of bed?': 'Yes.',
 'Did you ever have a wish come true?': 'No.',
 'Did you ever have the same dream more than once?': 'No.',
 'Did you ever plant a tree?': 'No.',
 'Did you ever ride in a wagon?': 'No.',
 'Did you ever spill paint?': 'Yes.',
 'Did you ever think that Saturday was a school day?': 'No.',
 'Did you ever win a big prize?': 'No.',
 'Did you have a dream last night?': 'No.',
 'Do you collect stamps?': 'Yes.',
 'Do you eat apples with the skin on?': 'No.',
 'Do you eat the crust on a sandwich?': 'Yes.',
 'Do you enjoy arts and crafts projects?': 'No.',
 'Do you ever listen to the radio?': 'Yes.',
 'Do you ever use a flashlight to read?': 'No.',
 'Do you fold your pizza before eating it?': 'No.',
 'Do you have a favorite TV show?': 'Yes.',
 'Do you have a favorite author?': 'Yes.',
 'Do you have a favorite book?': 'No.',
 'Do you have a favorite relative?': 'No.',
 'Do you have a favorite song?': 'No.',
 'Do you have a hero?': 'Yes.',
 'Do you have a pet fish?': 'No.',
 'Do you have a younger brother?': 'Yes.',
 'Do you have a younger sister?': 'Yes.',
 'Do you have an older brother?': 'No.',
 'Do you have an older sister?': 'No.',
 'Do you have blue eyes?': 'Yes.',
 'Do you have brown eyes?': 'Yes.',
 'Do you have curly hair?': 'No.',
 'Do you have freckles?': 'Yes.',
 'Do you have green eyes?': 'No.',
 'Do you have jobs to do at home?': 'Yes.',
 'Do you know any triplets?': 'Yes.',
 'Do you know how to make a meal?': 'No.',
 'Do you know someone named Barbara?': 'No.',
 'Do you know someone named Bob?': 'Yes.',
 'Do you know someone who is very old?': 'No.',
 'Do you know what you want to be when you grow up?': 'Yes.',
 'Do you lick the frosting off the cupcake?': 'Yes.',
 'Do you like any foods that are round?': 'No.',
 'Do you like any green food?': 'Yes.',
 'Do you like being in high places?': 'Yes.',
 'Do you like big dogs?': 'No.',
 'Do you like books without pictures?': 'No.',
 'Do you like fireworks?': 'No.',
 'Do you like red gumballs?': 'Yes.',
 'Do you like the taste of cranberry sauce?': 'Yes.',
 'Do you like the taste of onions?': 'Yes.',
 'Do you like to draw?': 'Yes.',
 'Do you like to dress in costumes?': 'No.',
 'Do you like to eat broccoli?': 'No.',
 'Do you like to eat ketchup on eggs?': 'Yes.',
 'Do you like to eat mushrooms?': 'No.',
 'Do you like to eat raisins?': 'Yes.',
 'Do you like to eat spinach?': 'No.',
 'Do you like to feel the wind?': 'Yes.',
 'Do you like to hang upside-down?': 'Yes.',
 'Do you like to ice-skate?': 'Yes.',
 'Do you like to play in mud?': 'No.',
 'Do you like to play in rain?': 'Yes.',
 'Do you like to play in sand?': 'Yes.',
 'Do you like to play in snow?': 'Yes.',
 'Do you like to play video games?': 'Yes.',
 'Do you like to play with blocks?': 'Yes.',
 'Do you like to shake pepper on your food?': 'Yes.',
 'Do you like to shop for food?': 'Yes.',
 'Do you like to walk on tip-toes?': 'Yes.',
 'Do you like to write in a journal?': 'Yes.',
 'Do you like winter best?': 'Yes.',
 'Do you live in an apartment building?': 'Yes.',
 'Do you own a belt?': 'Yes.',
 'Do you own a pet cat?': 'Yes.',
 'Do you own a pet dog?': 'No.',
 'Do you own a red umbrella?': 'Yes.',
 'Do you own a striped sweater?': 'No.',
 'Do you own yellow socks?': 'No.',
 'Do you play a sport where you wear a helmet?': 'No.',
 'Do you remember your dreams?': 'No.',
 'Do you ride a bus to school?': 'No.',
 'Do you think computers are smarter than people?': 'No.',
 'Do you think every problem has a solution?': 'No.',
 'Do you think grown-ups are lucky?': 'Yes.',
 'Do you think it is ever a good idea to shout?': 'Yes.',
 'Do you think it would be fun to be a clown?': 'Yes.',
 'Do you think you will live to be 100 years old?': 'No.',
 'Do you try and stay up later than your bedtime?': 'Yes.',
 'Do you walk to school?': 'No.',
 'Do you want a haircut soon?': 'Yes.',
 'Do you watch TV?': 'No.',
 'Do you wear socks when you go to bed?': 'Yes.',
 'Do you wish there were no rules in school?': 'No.',
 'Do you wish you could be invisible for one day?': 'Yes.',
 'Do you wish you could fly?': 'Yes.',
 'Do you wish you could see a real live dino?': 'Yes.',
 'Do you wish you could stay up all night long?': 'Yes.',
 'Do you wish you could walk on your hands?': 'No.',
 'Do you wish you had a homework machine?': 'No.',
 'Do you wish you had four arms?': 'Yes.',
 'Do you wish you lived all alone?': 'No.',
 'Do you wish you lived in the days of the dino?': 'No.',
 'Do you wish you were a grown-up?': 'Yes.',
 'Do you wish you were as flat as a piece of paper?': 'Yes.',
 'Have you ever been bowling?': 'No.',
 'Have you ever been confused?': 'No.',
 'Have you ever been in a castle?': 'Yes.',
 'Have you ever been in a treehouse?': 'No.',
 'Have you ever been lost?': 'Yes.',
 'Have you ever been really angry?': 'Yes.',
 'Have you ever been really surprised?': 'Yes.',
 'Have you ever been worried?': 'Yes.',
 'Have you ever broken a bone?': 'Yes.',
 'Have you ever broken anything?': 'Yes.',
 'Have you ever camped out in a tent?': 'Yes.',
 'Have you ever climbed a fence?': 'Yes.',
 'Have you ever climbed a mountain?': 'No.',
 'Have you ever danced on a stage?': 'No.',
 'Have you ever done a chore without being asked?': 'No.',
 'Have you ever dropped an ice cream cone?': 'No.',
 'Have you ever dug a deep hole?': 'Yes.',
 'Have you ever earned money to do a job?': 'Yes.',
 'Have you ever enjoyed a picnic?': 'Yes.',
 'Have you ever felt very lucky?': 'Yes.',
 'Have you ever felt very unlucky?': 'Yes.',
 'Have you ever flown a kite?': 'No.',
 'Have you ever found money?': 'No.',
 'Have you ever gone swimming in an ocean?': 'Yes.',
 'Have you ever had a bad haircut?': 'No.',
 'Have you ever had a ride in a convertible car?': 'Yes.',
 'Have you ever had a scary dream?': 'Yes.',
 'Have you ever had an X-ray?': 'Yes.',
 'Have you ever held a frog?': 'Yes.',
 'Have you ever held a little kitten?': 'No.',
 'Have you ever held a newborn baby?': 'Yes.',
 'Have you ever helped a friend?': 'Yes.',
 'Have you ever hopped on a pogo stick?': 'Yes.',
 'Have you ever jumped on a trampoline?': 'Yes.',
 'Have you ever lost a library book?': 'Yes.',
 'Have you ever lost something really important?': 'No.',
 'Have you ever lost your shoes?': 'Yes.',
 'Have you ever met a book author?': 'No.',
 'Have you ever met a famous person?': 'Yes.',
 'Have you ever painted a room?': 'No.',
 'Have you ever picked apples from a tree?': 'Yes.',
 'Have you ever planned a secret surprise': 'No.',
 'Have you ever played a team sport?': 'Yes.',
 'Have you ever played in a pit filled with plastic balls?': 'No.',
 'Have you ever played laser tag?': 'No.',
 'Have you ever pretended you were a great singer?': 'No.',
 'Have you ever put on a show for grown-ups?': 'No.',
 'Have you ever received a letter in the mail?': 'Yes.',
 'Have you ever ridden on a donkey?': 'Yes.',
 'Have you ever ridden on a horse?': 'No.',
 'Have you ever rolled down a hill?': 'No.',
 'Have you ever seen a full moon?': 'No.',
 'Have you ever seen a magician perform?': 'Yes.',
 'Have you ever seen a parade?': 'Yes.',
 'Have you ever seen a waterfall?': 'Yes.',
 'Have you ever seen an ant farm?': 'No.',
 'Have you ever slammed a door on purpose?': 'Yes.',
 'Have you ever spilled anything?': 'No.',
 'Have you ever splashed in rain puddles?': 'No.',
 'Have you ever stayed awake until midnight?': 'No.',
 'Have you ever touched a real snake?': 'No.',
 'Have you ever traveled in a plane or a jet?': 'Yes.',
 'Have you ever traveled on a train?': 'No.',
 'Have you ever traveled out of the country?': 'Yes.',
 'Have you ever visited a farm?': 'Yes.',
 'Have you ever visited a museum?': 'No.',
 'Have you ever walked across a bridge?': 'Yes.',
 'Have you ever won a prize?': 'Yes.',
 'Have you ever written a Thank You note?': 'No.',
 'Have you ever written a book?': 'Yes.',
 'Have you taken a trip on a boat?': 'No.',
 'Is chocolate ice-cream your favorite dessert?': 'No.',
 'Is your hair straight?': 'Yes.',
 'Were you born in this community?': 'No.',
 'When you grow up, will you like the taste of coffee?': 'Yes.',
 'Would you ever travel into outer space?': 'Yes.',
 'Would you like to be President of the United States?': 'Yes.',
 'Would you like to be a kid forever?': 'No.',
 'Would you like to be one inch tall?': 'No.',
 'Would you like to run the school?': 'Yes.',
 'Would you like to travel into space?': 'Yes.',
 'Would you want a pet monkey?': 'Yes.',
 'Would you want to own a pet lion?': 'No.',
 'for someone?': 'No.'}

#Create 10 questionnaires.
for quizNum in range(30):
    #Create questionnaire file & answer file.
    questionFile = open("Dan's Questionnaire #%s.txt" % (quizNum + 1), "w")
    answerFile = open("Dan's Questionnare #%s (Answers).txt" % (quizNum + 1), "w")

    #Add header to questionnaire file & answer file.
    questionFile.write("HOW MUCH DO YOU KNOW ABOUT ME?".center(30, "=") + "\n\n")
    answerFile.write("HOW MANY ANSWERS YOU GET RIGHT?".center(30, "=") + "\n\n")

    #Shuffle questions.
    questions = list(questionnaire.keys())
    random.shuffle(questions)

    #Write out 30 questions for questionnaire.
    for questionNum in range(15):

        #Grab the correct answer.
        correctAnswer = questionnaire[questions[questionNum]]

        #Write question into question file.
        questionFile.write(questions[questionNum].ljust(50, ".") + "\t YES or NO" + "\n\n")

        #Write question & answer in answer file.
        answerFile.write(questions[questionNum].ljust(50, ".") + "\t" + correctAnswer + "\n\n")

    questionFile.close()
    answerFile.close()
