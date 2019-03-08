# voter คือจำนวนผู้ไปใช้สิทธิเลือกตั้งทั้งหมด
voter = int(input("Number of Voter: "))

# mhr คือจำนวน ส.ส. 1 คนในพรรคที่จะได้เข้าไปนั่งในสภา
mhr = voter / 500

# all_vote คือ คะแนนรวมของพรรคการเมืองรวมทุกเขต
all_vote = int(input("Vote Score of Party of mhr: "))

# all_mhr คือ จำนวน ส.ส.พรรคทั้งหมดที่จะได้เข้าไปนั่งในสภา
all_mhr = all_vote / mhr

# dst_mht คือ จำนวนเขตที่ส.ส.ของพรรคชนะโหวต
dst_mhr = int(input("All District that the party win: "))

# ptl_mhr คือ จำนวน ส.ส.ปาร์ตี้ลิสต์ทั้งหมดที่พรรคจะได้มา
ptl_mhr = all_mhr - dst_mhr

if(ptl_mhr <= 0):
    ptl_mhr = 0

print("มีจำนวนผู้ไปใช้สิทธิ {} คน\n\nสส 1 คนต้องใช้คะแนน {} โหวต\n\nพรรค ABC ได้คะแนนโหวตทั้งประเทศรวม {} โหวต\n\nดังนั้นพรรค ABC จะได้ สส เข้าไปนั่งในสภา {} คน\n\nพรรค ABC ชนะไปทั้งหมด {} เขต\n\nดังนั้นพรรค ABC จะได้ สส ปาร์ตี้ลิสต์ไปทั้งหมด {} คน".format(voter,mhr,all_vote,all_mhr,dst_mhr,ptl_mhr))

