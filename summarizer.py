from text_summarizer_model import TextSummarizer

if __name__ == '__main__':
    model = TextSummarizer()
    sample_texts = [
        """
        Education enables individuals to develop the knowledge, skills and confidence needed to participate fully in society. 
        Through teaching and learning, societies pass on essential knowledge, values and competencies across generations.
        Education builds foundational literacy and numeracy, strengthens social and emotional skills and equips people to make
        informed choices about their lives and their communities.

        Education is one of the most powerful tools for lifting excluded children and adults out of poverty and is an enabler of
        other fundamental human rights. It is a cornerstone of peace, justice, and resilience in the face of today’s most pressing
        global challenges. It forms the foundation of democratic society, and the right to education is protected under international law. 

        To achieve the right to education for all, education must be inclusive, equitable and free from discrimination. UNESCO works
        closely with Member States and partners to uphold these principles and strengthen education systems worldwide to make sure no
        learner is left behind. 
        """,
        """
        Geneva—Rolex released its new timepieces on Tuesday as Watches and Wonders Geneva, the week-long trade show dedicated to the
        horological world, kicked off in Switzerland.

        All of the new models Rolex is debuting in 2026 are Oyster Perpetual watches, the brand’s first waterproof wristwatch, which
        debuted in 1926 and is turning 100 this year.

        Alongside the eight watch debuts came three new testing criteria for Rolex’s Superlative Chronometer Certification that was
        redefined in 2015.

        The criteria are: resistance to magnetism, reliability, and sustainability, and are now implemented during the design and manufacturing
        stage, Rolex said.

        The certification is symbolized by a green seal that reads “Superlative Certified” and is controlled by internationally recognized,
        independent Swiss entities.

        Commenting on Rolex’s debuts, Bob’s Watches CEO Paul Altieri said, “Overall, Rolex played it conservative this year.

        “The centenary theme gave them cover to keep things restrained. But that Oyster Perpetual 36 with the multicolored Jubilee dial is
        genuinely fun. It’s unexpected from Rolex, and I mean that as a compliment.” 
        
        The new Oyster Perpetual 41 is “a tribute to the very essence of time,” Rolex said.

        The Rolesor version of the timepiece references the case elements of early Oyster watches, with touches of yellow gold on the bezel
        and winding crown, while the case and bracelet are Oystersteel.

        It also features the number 100 on the winding crown and “100 years” in place of the usual “Swiss Made” marking under 6 o’clock on
        the slate dial.

        “Replacing ‘Swiss Made’ with ‘100 years’ at 6 o’clock is something Rolex almost never does,” Altieri noted.

        “The slate dial, green accents, and yellow Rolesor details keep it understated, but this is one of the clearest statements of heritage
        Rolex has ever made.”
        """,
        """
        Pakistan, officially the Islamic Republic of Pakistan, is a country in South Asia. It is the fifth-most populous country, with a population
        of over 241.5 million, having the second-largest Muslim population as of 2023. Islamabad is the nation's capital, while Karachi is its largest
        city and financial centre. Pakistan is the 33rd-largest country by area. Bounded by the Arabian Sea on the south, the Gulf of Oman on the
        southwest, and the Sir Creek on the southeast, it shares land borders with India to the east; Afghanistan to the west; Iran to the southwest;
        and China to the northeast. It shares a maritime border with Oman in the Gulf of Oman, and is separated from Tajikistan in the northwest by
        Afghanistan's narrow Wakhan Corridor.

        Pakistan is the site of several ancient cultures, including the 8,500-year-old Neolithic site of Mehrgarh in Balochistan, the Indus Valley
        Civilisation of the Bronze Age, and the ancient Gandhara civilisation. The regions that compose the modern state of Pakistan were 
        realm of multiple empires and dynasties, including the Achaemenid, the Maurya, the Kushan, the Gupta; the Umayyad Caliphate in its southern
        regions, the Hindu Shahis, the Ghaznavids, the Delhi Sultanate, the Samma, the Shah Miris, the Mughals, and finally, the British Raj from 1858
        to 1947.

        Spurred by the Pakistan Movement, which sought a homeland for the Muslims of British India, and election victories in 1946 by the All-India
        Muslim League, Pakistan gained independence in 1947 after the partition of British India, which awarded separate statehood to its
        Muslim-majority regions and was accompanied by an unparalleled mass migration and loss of life. Initially a dominion of the British
        Commonwealth, Pakistan adopted a republican constitution in 1956 and became an Islamic republic with two geographically separate provinces, 
        East Pakistan and West Pakistan. East Pakistan seceded as the new country of Bangladesh in 1971 after a nine-month-long civil war. In the
        following four decades, Pakistan has been ruled by governments that alternated between civilian and military, democratic and authoritarian,
        relatively secular and Islamist.
        """
    ]
    
    for text in sample_texts:
        print("text")
        print(text, '\n')
        
        response = model.summarize(text)
        
        print("response")
        print(print)
        print('='*40)