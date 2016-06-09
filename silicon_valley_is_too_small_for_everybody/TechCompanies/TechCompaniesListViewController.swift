//
//  TechCompaniesListViewController.swift
//  TechCompanies
//
//  Created by Bennett Buchanan on 6/8/16.
//  Copyright © 2016 Bennett Buchanan. All rights reserved.
//

import UIKit

class TechCompaniesListViewController: UITableViewController {
    
    var schoolList:[Entity]!
    var techCompanyList:[Entity]!
    let techDetailSegue = "techDetailSegue"

    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.title = "Entity list"
        techCompanyList = EntitiesHelper.getTechCompanies()
        schoolList = EntitiesHelper.getSchools()
        

        // Uncomment the following line to preserve selection between presentations
        // self.clearsSelectionOnViewWillAppear = false

        // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
        // self.navigationItem.rightBarButtonItem = self.editButtonItem()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    // MARK: - Table view data source

    override func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        // #warning Incomplete implementation, return the number of sections
        // Update to reflect maleable section numbers.
        return EntityType.TechCompany.hashValue
    }

    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // #warning Incomplete implementation, return the number of rows
        if section == 0 {
            return schoolList.count
        } else {
            return techCompanyList.count
        }
    }
    
    override func tableView(tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        if section == 0 {
            return "School"
        } else {
            return "TechCompany"
        }
    }

    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCellWithIdentifier("techCell", forIndexPath: indexPath)
        
        if indexPath.section == 0 {
            cell.textLabel?.textAlignment = NSTextAlignment.Center
            cell.textLabel?.text = schoolList[indexPath.row].name
            cell.detailTextLabel?.text = "I love studying"
            cell.imageView?.image = UIImage(named: schoolList[indexPath.row].imageName)
        } else {
            cell.textLabel?.textAlignment = NSTextAlignment.Center
            cell.textLabel?.text = techCompanyList[indexPath.row].name
            cell.detailTextLabel?.text = "I love working"
            cell.imageView?.image = UIImage(named: techCompanyList[indexPath.row].imageName)
        }

        return cell
    }


    /*
    // Override to support conditional editing of the table view.
    override func tableView(tableView: UITableView, canEditRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return false if you do not want the specified item to be editable.
        return true
    }
    */

    /*
    // Override to support editing the table view.
    override func tableView(tableView: UITableView, commitEditingStyle editingStyle: UITableViewCellEditingStyle, forRowAtIndexPath indexPath: NSIndexPath) {
        if editingStyle == .Delete {
            // Delete the row from the data source
            tableView.deleteRowsAtIndexPaths([indexPath], withRowAnimation: .Fade)
        } else if editingStyle == .Insert {
            // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
        }    
    }
    */

    /*
    // Override to support rearranging the table view.
    override func tableView(tableView: UITableView, moveRowAtIndexPath fromIndexPath: NSIndexPath, toIndexPath: NSIndexPath) {

    }
    */

    /*
    // Override to support conditional rearranging of the table view.
    override func tableView(tableView: UITableView, canMoveRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return false if you do not want the item to be re-orderable.
        return true
    }
    */


    // MARK: - Navigation
    
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        if segue.identifier == "techDetailSegue" {
            if let destination = segue.destinationViewController as? TechCompanyDetailViewController {
                
                let path = tableView.indexPathForSelectedRow
                if path!.section == 0 {
                    destination.entity = schoolList[path!.row]
                } else {
                    destination.entity = techCompanyList[path!.row]
                }

            
            }
        }
    }
    
//    // In a storyboard-based application, you will often want to do a little preparation before navigation
//    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
//        // Get the new view controller using segue.destinationViewController.
//        // Pass the selected object to the new view controller.
//        if segue.identifier == "techDetailSegue" {
//            let _ = segue.destinationViewController as? TechCompanyDetailViewController
//        }
//    }
}
