import open3d as o3d
import numpy as np
from collections import defaultdict

def trim_bounding_box(bbox, offsets):
  min_bound = bbox.get_min_bound()
  max_bound = bbox.get_max_bound()
  center = (min_bound + max_bound) / 2.0  # Calculate the center of the bounding box

    # Halve the desired size along z and x axes
  new_size = [(max_bound[0] - min_bound[0])/2, (max_bound[2] - min_bound[2]) / 2.5, int((max_bound[1]- min_bound[1])/1.75)]

    # Calculate new minimum and maximum bounds based on center and half-size
  trimmed_min = [center[i] - new_size[i] / 2.0 for i in range(3)]
  trimmed_max = [center[i] + new_size[i] / 2.0 for i in range(3)]
  """
  Trims the edges of a bounding box by specified offsets.

  Args:
      bbox: An o3d.geometry.AxisAlignedBoundingBox3d object.
      offsets: A list of [xmin_offset, ymin_offset, zmin_offset, xmax_offset, ymax_offset, zmax_offset].

  Returns:
      A trimmed o3d.geometry.AxisAlignedBoundingBox3d object.
  """

    
  return o3d.geometry.AxisAlignedBoundingBox(trimmed_min, trimmed_max)

# Load point cloud
pcd = o3d.io.read_point_cloud("py_HLTRGB_3_Overlay.ply")
print(f"Loaded point cloud with {len(pcd.points)} points.")

# Get basic statistics
points = np.asarray(pcd.points)
min_coords = points.min(axis=0)
max_coords = points.max(axis=0)
dimensions = max_coords - min_coords
print(f"Point cloud dimensions: {dimensions}")

# Statistical outlier removal
cl, ind = pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)
pcd_filtered = pcd.select_by_index(ind)
print(f"After outlier removal: {len(pcd_filtered.points)} points.")



# Voxel downsampling
voxel_size = min(dimensions) / 100  # Adaptive voxel size
voxel_size = voxel_size / 3
pcd_down = pcd_filtered.voxel_down_sample(voxel_size)
print(f"After downsampling: {len(pcd_down.points)} points.")

# DBSCAN clustering
eps = voxel_size * 2  # Adjust this multiplier if needed
min_points = 10  # Adjust based on your data
labels = np.array(pcd_down.cluster_dbscan(eps=eps, min_points=min_points))
max_label = labels.max()
print(f"Number of clusters: {max_label + 1}")

# Visualization
vis = o3d.visualization.Visualizer()
vis.create_window()

if max_label >= 0:
    # Find the largest cluster
    unique, counts = np.unique(labels, return_counts=True)
    largest_cluster = unique[int(np.argmax(counts[1:])+1)]  # Skip -1 (noise)
    
    # Extract the largest cluster
    object_points = pcd_down.select_by_index(np.where(labels != largest_cluster)[0])
    
    # Create a bounding box for the object
    bbox = object_points.get_axis_aligned_bounding_box()
    trim_offsets = [-10, -10, -10, 30, 15, 30]  # Example offsets (modify as needed)
    trimmed_bbox = trim_bounding_box(bbox, trim_offsets)
    bbox=trimmed_bbox
    bbox.color = [1, 0, 0]  # Red color for the bounding box
    
    # Add the object points and bounding box
    vis.add_geometry(object_points)
    vis.add_geometry(bbox)
    print(f"Largest cluster has {len(object_points.points)} points.")
else:
    # If no clusters found, show the entire downsampled point cloud
    vis.add_geometry(pcd_down)
    print("No clusters found. Showing entire point cloud.")

# Set up the view
vis.get_render_option().point_size = 2
#vis.get_render_option().background_color = [0.1, 0.1, 0.1]  # Dark background

# Optimize the camera view
vis.get_view_control().set_front([0, 0, -1])
vis.get_view_control().set_up([0, -1, 0])
vis.get_view_control().set_zoom(0.8)

# Run the visualizer
vis.run()
vis.destroy_window()