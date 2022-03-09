import sys
sys.path.append(r'C:/Users/bp/Documents/GitHub/investing_subscribe/DAO')
import DAO

def superChatInput(info_list):
    DAO.insert_super_chat(info_list[0],
                          info_list[1],
                          info_list[2],
                          info_list[3],
                          info_list[4],
                          info_list[5],
                          info_list[6],
                          info_list[7],
                          info_list[8],
                          info_list[9],
                          )