//
//  EntititesHelper.swift
//  TechCompanies
//
//  Created by Bennett Buchanan on 6/8/16.
//  Copyright © 2016 Bennett Buchanan. All rights reserved.
//

import UIKit

class EntitiesHelper {
    static var listOfSchool:[Entity]! = []
    static var listOfTechCompany:[Entity]! = []
    static var entireList:[Entity]! = []
    
    static func getSchools() -> [Entity]! {
        if listOfSchool.count == 0 {
            listOfSchool.append(Entity(name: "Holberton", town: "San Francisco", imageName: "holberton", type: .School))
        }
        return listOfSchool
    }
    
    static func getTechCompanies() -> [Entity]! {
        if listOfTechCompany.count == 0 {
            listOfTechCompany.append(Entity(name: "Linkedin", town: "San Francisco", imageName: "linkedin", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Docker", town: "San Francisco", imageName: "docker", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Google", town: "Mountain View", imageName: "google", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Yahoo", town: "Sunnyvale", imageName: "yahoo", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Apple", town: "Cupertino", imageName: "apple", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Twitter", town: "San Francisco", imageName: "twitter", type: .TechCompany))
        }
        return listOfTechCompany
    }
    static func getEntireList() -> [Entity]! {
        for e in listOfTechCompany {
            entireList.append(e)
        }
        for e in listOfSchool {
            entireList.append(e)
        }
        return entireList
    }
}

