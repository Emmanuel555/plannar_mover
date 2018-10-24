#!/usr/bin/env python
import rospy
import rospack
import time
from geometry_msgs.msg import Pose
from get_model_gazebo_pose import GazeboModel

class ModelPoseStore():
    def __init__(self, model_to_track_list):
        
        
        
        # This are the models that we will generate information about.
        self.model_to_track_name = "demo_spam1"
        self.table_to_track_name = "demo_table1"
        
        model_to_track_list = [self.model_to_track_name, self.table_to_track_name]
        self.gz_model_obj = GazeboModel(model_to_track_list)
        
        
    def get_pose_of_model(self, model_name):
        """
        Retrieves the position of an object from the world
        """
        pose_now = self.gz_model_obj.get_model_pose(model_name)
        
        return pose_now
        
    def store_model_poses_for_duration(self, model_name, duration=1.0, file_to_store="poses.yaml"):
        """
        We store in the Given File Name the poses of the given model, whihc has to be inside the init model list
        inside a Yaml file
        """
        
        
        
    
    

if __name__ == '__main__':
    rospy.init_node('store_model_poses_node', anonymous=True, log_level=rospy.WARN)
    
    model_to_save_poses = "custom_ground_plane_box"
    model_to_track_list = [model_to_save_poses]
    model_pose_store_obj = ModelPoseStore(model_to_track_list)
    
    rospack = rospkg.RosPack()
    # get the file path for rospy_tutorials
    path_to_package = rospack.get_path('plannar_mover')
    pose_files_dir = os.path.join(path_to_package, "pose_files")
    
    
    if not os.path.exists(pose_files_dir):
        os.makedirs(pose_files_dir)
    
    
    pose_file_name = model_to_save_poses+str(time.time())+".yaml"
    pose_file_path = os.path.join(pose_files_dir, pose_file_name)
    
    
    model_pose_store_obj.store_model_poses_for_duration(    model_name=model_to_track_list[0],
                                                            duration=1.0,
                                                            file_to_store=pose_file_path)