import  requests




def getMoveinfo(url):
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "text/html,application/xhtml+xml",
        "Cookie": "_lxsdk_cuid="
    }
    response = session.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None

def saveItem(dbName, moveId, id, originalData) :
    conn = sqlite3.connect(dbName)
    conn.text_factory=str
    cursor = conn.cursor()
    ins="INSERT OR REPLACE INTO comments values (?,?,?)"
    v = (id, originalData, moveId)
    cursor.execute(ins,v)
    cursor.close()
    conn.commit()
    conn.close()

def convert(dbName):
    conn = sqlite3.connect(dbName)
    conn.text_factory = str
    cursor = conn.cursor()
    cursor.execute("select * from comments")
    data = cursor.fetchall()
    for item in data:
        commentItem = json.loads(item[1])
        movieId = item[2]
        insertItem(dbName, movieId, commentItem)
    cursor.close()
    conn.commit()
    conn.close()

def insertItem(dbName, movieId,  item):
    conn = sqlite3.connect(dbName)
    conn.text_factory = str
    cursor = conn.cursor()
    sql = '''
    INSERT OR REPLACE INTO convertData values(?,?,?,?,?,?,?,?,?)
    '''
    values = (
        getValue(item, "id"),
        movieId,
        getValue(item, "userId"),
        getValue(item, "nickName"),
        getValue(item, "score"),
        getValue(item, "content"),
        getValue(item, "cityName"),
        getValue(item, "vipType"),
        getValue(item, "startTime"))
    cursor.execute(sql, values)
    cursor.close()
    conn.commit()
    conn.close()


data = pd.read_sql("select * from convertData", conn)
    city = data.groupby(['cityName'])
    city_com = city['score'].agg(['mean','count'])
    city_com.reset_index(inplace=True)
    fo = open("citys.json",'r')
    citys_info = fo.readlines()
    citysJson = json.loads(str(citys_info[0]))
    print city_com
    data_map_all = [(getRealName(city_com['cityName'][i], citysJson),city_com['count'][i]) for i in range(0,city_com.shape[0])]
    data_map_list = {}
    for item in data_map_all:
        if data_map_list.has_key(item[0]):
            value = data_map_list[item[0]]
            value += item[1]
            data_map_list[item[0]] = value
        else:
            data_map_list[item[0]] = item[1]
    data_map = [(realKeys(key), data_map_list[key] ) for key in data_map_list.keys()]

attr = ["灭霸","美国队长",
        "钢铁侠", "浩克", "奇异博士",  "蜘蛛侠", "索尔" ,"黑寡妇",
        "鹰眼", "惊奇队长", "幻视",
        "猩红女巫","蚁人", "古一法师"]

alias = {
    "灭霸": ["灭霸", "Thanos"],
    "美国队长": ["美国队长", "美队"],
    "浩克": ["浩克", "绿巨人", "班纳", "HULK"],
    "奇异博士": ["奇异博士", "医生"],
    "钢铁侠": ["钢铁侠", "stark", "斯塔克", "托尼", "史塔克"],
    "蜘蛛侠": ["蜘蛛侠","蜘蛛","彼得", "荷兰弟"],
    "索尔":["索尔", "雷神"],
    "黑寡妇": ["黑寡妇", "寡姐"],
    "鹰眼":["鹰眼","克林顿","巴顿","克林特"],
    "惊奇队长":["惊奇队长","卡罗尔", "惊奇"],
    "星云":["星云"],
    "猩红女巫": ["猩红女巫", "绯红女巫", "旺达"],
    "蚁人":["蚁人", "蚁侠", "Ant", "AntMan"],
    "古一法师": ["古一", "古一法师", "法师"]
}
v1 = [getCommentCount(getAlias(alias, attr[i])) for i in range(0, len(attr))]
bar = Bar("Hiro")
bar.add("count",attr,v1,is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
    xaxis_interval=0,is_splitline_show=True)
bar.render("html/hiro_count.html")

def emotionParser(name):
    conn = conn = sqlite3.connect("end.db")
    conn.text_factory = str
    cursor = conn.cursor()
    likeStr = "like \"%" + name + "%\""
    cursor.execute("select content from convertData where content " + likeStr)
    values = cursor.fetchall()
    sentimentslist = []
    for item in values:
        sentimentslist.append(SnowNLP(item[0].decode("utf-8")).sentiments)
    plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01), facecolor="#4F8CD6")
    plt.xlabel("Sentiments Probability")
    plt.ylabel("Quantity")
    plt.title("Analysis of Sentiments for " + name)
    plt.show()
    cursor.close()
    conn.close()