from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
from datetime import datetime

class Project:
    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.user_id = data_dict['user_id']
        self.title = data_dict['title']
        self.model = data_dict['model']
        self.category = data_dict['category']
        self.description = data_dict['description']
        self.pitch = data_dict['pitch']
        self.status = data_dict['status']
        self.capital = data_dict['capital']
        self.goal = data_dict['goal']
        self.amount_raised = data_dict['amount_raised']
        self.deadline = data_dict['deadline']
        self.tax_code = data_dict['tax_code']
        self.bank_details = data_dict['bank_details']
        self.acceptance_date = data_dict['acceptance_date']
        self.image = data_dict['image']
        self.video = data_dict['video']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.investors = []

    #======================CREATE==========================

    @classmethod
    def create_project(cls, data_dict):
        query = """
                INSERT INTO projects (user_id, title, model,category,description,pitch,status,capital,goal,amount_raised,deadline,
                tax_code,bank_details,business_plan,image,video) 
                VALUES (%(user_id)s,%(title)s,%(model)s,%(category)s,%(description)s,%(pitch)s,%(status)s,%(capital)s,%(goal)s,%(amount_raised)s,%(deadline)s,
                %(tax_code)s,%(bank_details)s,%(business_plan)s,%(image)s,
                %(video)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data_dict)
    
    # --------------- GET PROJECT BY USER ID ----------------
    @classmethod
    def get_project_by_user_id(cls, data_dict):
        query = """
                    SELECT * FROM projects WHERE user_id = %(user_id)s;
                """
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        if result:
            return cls(result[0])
        return False
    
    # --------------- GET PROJECT BY ID ----------------
    @classmethod
    def get_project_by_id(cls, data_dict):
        query = """
                    SELECT * FROM projects WHERE id = %(id)s;
                """
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        if result:
            return cls(result[0])
        return False
    
    # ------- GET ALL PROJECTS -----------------
    @classmethod
    def get_all_projects(cls):
        query = "SELECT * FROM projects;"
        result = connectToMySQL(DATABASE).query_db(query)
        all_projects = []
        for row in result:
            project = cls(row)
            all_projects.append(project)
        return all_projects